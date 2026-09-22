# Kiến trúc Data Pipeline — Credit Scoring Default Rate

Tài liệu này mô tả chi tiết kiến trúc luồng dữ liệu của hệ thống chấm điểm rủi ro vỡ nợ tín dụng, chuẩn hóa theo luồng thực thi chính thức (**Production Pipeline: Bước 1 → 2 → 3 → 4**). Mô hình lõi 23 biến đã được thay thế bằng mô hình baseline 8 biến; **Bước 4** là Risk Adjustment áp trực tiếp trên nền dự đoán baseline.

---

## 1. Sơ đồ Luồng Tổng thể

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│          LUỒNG CHÍNH THỨC (PRODUCTION PIPELINE): BƯỚC 1 ──▶ BƯỚC 2 ──▶ BƯỚC 3 ──▶ BƯỚC 4     │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                              │
│   ┌───────────────────┐       ┌───────────────────┐       ┌───────────────────┐               │
│   │   BƯỚC 1 (step_1) │       │   BƯỚC 2 (step_2) │       │   BƯỚC 3 (step_3) │               │
│   │                   │       │                   │       │                   │               │
│   │    Bóc tách Excel │──────▶│  Baseline 8 biến  │──────▶│ Dự đoán Baseline  │               │
│   │  & Mã hóa Định    │       │  thô Logistic     │       │  & tách theo      │               │
│   │  tính (Train/Test)│       │  (chưa chuẩn hóa) │       │  target (0/1)     │               │
│   └───────────────────┘       └───────────────────┘       └───────────────────┘               │
│            │                             │                                  │                │
│            ▼                             ▼                                  ▼                │
│        train.csv                     model.pkl                  prediction_test.csv           │
│        test.csv                   train_final.csv            has_default (1.422) / non (5.092)│
│    label_encoders.json           (Acc train ~69.3%)              (Acc test ~70.14%)            │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│   ┌───────────────────────────────────────────┐                                                │
│   │          BƯỚC 4 (step_4)                 │                                                 │
│   │      Risk Adjustment (Lớp GỠ / VỚT)      │                                                 │
│   │  - Tự dựng 4 biến tương tác nghiệp vụ    │                                                 │
│   │  - Áp trực tiếp trên nền dự đoán Bước 3  │                                                 │
│   └───────────────────────────────────────────┘                                                │
│              │                                                                                 │
│              ▼                                                                                 │
│      prediction_final_evaluated                                                                │
│             rescued_fp.csv (310)                                                               │
│             caught_fn.csv (52)                                                                 │
│   (Acc: 73.06% | FP: 1,164 ca | TN: 3,928 ca)                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Chi tiết Luồng Chính (Production Flow)

> **Quy ước tên gọi nghiệp vụ:** luồng chính gồm **Bước 1** (Tiền xử lý) → **Bước 2** (Baseline) → **Bước 3** (Dự đoán baseline) → **Bước 4** (Risk Adjustment). Thư mục mã nguồn tương ứng là `step_1` → `step_2` → `step_3` → `step_4`.

### Bước 1: `step_1` — Tiền xử lý & Phân tách Dữ liệu
- **Đầu vào**: `repo_source/step_1/input/Credit Risk Dataset Chính.xlsx` (32,566 dòng, sheet *Dữ liệu rủi ro tín dụng*).
- **Xử lý**:
  - Bảo toàn `Mã khách hàng` để phục vụ đối soát, truy vết sau mô hình.
  - Mã hóa Label Encoding cho 11 cột biến định tính (lưu `label_encoders.json`).
  - Phân tầng dữ liệu (Stratified Split 80/20 theo nhãn `Trạng thái trả nợ`):
    + Tập Huấn luyện (`train.csv`): 26,052 dòng.
    + Tập Kiểm thử (`test.csv`): 6,514 dòng.

### Bước 2: `step_2` — Mô hình Baseline (8 biến thô, chưa chuẩn hóa)
- **Đầu vào**: `train.csv` từ `step_1/output/` (26,052 dòng).
- **Xử lý**:
  - Rút gọn 8 biến thô: Lãi suất, LTI, DTI tổng, Thu nhập, Sở hữu nhà, Từng vỡ nợ, Số tiền vay, Mục đích vay.
  - Sinh `train_final.csv` rồi huấn luyện `LogisticRegression(max_iter=1000, class_weight='balanced')`.
- **Hiệu năng (Train)**: Accuracy ~69.34%, AUC ~0.7274.
- **Đầu ra**: `train_final.csv`, `model.pkl`, `metadata.json`.

### Bước 3: `step_3` — Dự đoán Baseline & tách theo target
- **Đầu vào**: `model.pkl` + `metadata.json` từ `step_2/output/` cùng `train.csv`/`test.csv` từ `step_1/output/`.
- **Xử lý**: sinh `*_final.csv`, dự đoán `predicted` + `prob_vỡ_nợ` + `correct`, tách theo target thật thành `prediction_test_non_default.csv` (5,092) và `prediction_test_has_default.csv` (1,422).
- **Hiệu năng (Test)**: Accuracy ~70.14%.
- **Đầu ra**: `prediction_test.csv`, `prediction_train.csv`, các file split has_default/non_default, `test_final.csv`, `train_final.csv`.

### Bước 4: `step_4` — Risk Adjustment (Lớp GỠ / Lớp VỚT) trên nền Baseline
- **Đầu vào**: `prediction_test_has_default.csv` và `prediction_test_non_default.csv` từ `step_3/output/` + `test.csv` từ `step_1/output/`.
- **Cơ chế hoạt động**:
  - Tự **dựng lại 4 biến tương tác nghiệp vụ** (`Tuong_tac_no_thue_nha`, `Tuong_tac_be_do_dong_tien`, `Tuong_tac_lti_lai_suat`, `Tuong_tac_bien_co_khancap`) từ dữ liệu `test.csv` (lấy thêm `Thâm niên làm việc (năm)` để tính bệ đỡ dòng tiền).
  - **Lớp GỠ (Rescue FP $\rightarrow$ TN)** — tổng 310 hồ sơ, cứu **264 FP**, chấp nhận chuyển **46 TP** sang FN (**Tỷ lệ 5.74 : 1**, toàn bộ ở Tầng 1 — dòng tiền & thâm niên; Tầng 2 BĐS an toàn không kích hoạt trên nền baseline).
  - **Lớp VỚT (Catch FN $\rightarrow$ TP — Bù trừ rủi ro)** — tổng 52 hồ sơ, bắt lại **12 ca nợ xấu tiềm ẩn**, chấp nhận **40 TN** chuyển sang FP:
    + *Tầng 1 (LTI $\times$ lãi suất cao)*: bắt lại 0 FN, mất 1 TN.
    + *Tầng 2 (Biến cố khẩn cấp & tiền sử nợ xấu)*: bắt lại 12 FN, mất 39 TN.
- **Kết quả đầu ra toàn hệ thống**:
  - **Accuracy**: **73.06%** (+2.92% so với baseline Bước 3).
  - **FP báo oan giảm sâu**: **1,164 ca** (giảm 224 ca oan).
  - **TN duyệt đúng khách tốt**: **3,928 ca** (+224 khách tốt).
  - **TP kiểm soát nợ xấu**: **831 ca**.
  - **FN**: **591 ca**.
- **Đầu ra**: `prediction_final_evaluated.csv`, `rescued_fp.csv`, `caught_fn.csv`, `step_4_hedging_report.json`, `step_4_ly_do_go_vot.md`, biểu đồ Lớp GỠ/VỚT, dữ liệu Deneb.

---

## 3. Hướng dẫn Vận hành

Môi trường thực thi sử dụng Virtualenv của dự án (`venv`):

### 3.1. Chạy Luồng chính thức (Mặc định)
Lệnh chạy trực tiếp chuỗi đầy đủ: `Bước 1 -> Bước 2 -> Bước 3 -> Bước 4`:
```bash
python repo_source/run_pipeline.py
```

### 3.2. Chạy riêng từng phần
Chạy riêng Bước 2 → 3 (tập con của luồng chính):
```bash
python repo_source/run_pipeline.py --benchmark-only
```

Cờ `--all` giữ tương thích, tương đương luồng chính 1→2→3→4:
```bash
python repo_source/run_pipeline.py --all
```

### 3.3. Đồng bộ Dữ liệu vào PostgreSQL
Nạp toàn bộ bảng dữ liệu từ tất cả các bước vào schema `credit_model`:
```bash
python repo_source/db_import.py
```
Lưu cấu trúc mô hình và các hệ số hồi quy (baseline `step_2`):
```bash
python repo_source/db_save_model.py
```

> **Lưu ý:** Bảng dữ liệu trong DB đã được nạp lại đúng luồng 4 bước mới (2026-09-21: 17 bảng dữ liệu + `step_2_model`/`step_2_model_coef`, không còn bảng `step_4_output_*`/`step_4_model` 23 biến/`step_5_*` — output CSV của step_4 đã xóa theo yêu cầu, chỉ giữ ảnh). Mô hình trên Power BI **chưa được sync lại**; đồng bộ khi có yêu cầu thông qua `step_4/sync_to_power_bi.py`.
