# Hiện trạng hệ thống — credit scoring default rate

## Server

| Server | IP/Domain | Vai trò | Trạng thái |
|---|---|---|---|
| *(chưa có)* | *(chưa có)* | *(chưa có)* | — |

## Services & Ports

| Service | Port | Mô tả | Trạng thái |
|---|---|---|---|
| *(chưa có)* | *(chưa có)* | *(chưa có)* | — |

## Database / Schema

- **Host**: localhost, PostgreSQL 18.4 (dịch vụ postgresql-x64-16 & postgresql-x64-18 đang chạy)
- **DB name**: `postgres`
- **User**: `hnv`
- **Schema**: `credit_model`
- **Script import**: `repo_source/db_import.py` (cài psycopg2-binary 2.9.13 trong venv)
- **Quy ước bảng**: `step_{N}_{input|output}_{tên file}` — nạp lại **2026-09-21** (29 bảng, 249.106 dòng). Bảng `step_4_input_test` (6,514) đã được khôi phục.
  - step_1: `step_1_output_test` (6,514), `step_1_output_train` (26,052)
  - step_2: `step_2_input_train` (26,052), `step_2_output_train_final` (26,052)
  - step_3: input test/train; output `prediction_test`, `prediction_test_has_default` (1,422), `prediction_test_non_default` (5,092), `prediction_train`, `prediction_train_has_default` (5,685), `prediction_train_non_default` (20,367), `test_final`, `train_final`
  - step_4 (Risk Adjustment): hiện **đã xóa toàn bộ file chỉ giữ `input/`** theo yêu cầu user 2026-09-21 (`da5fea5`); sau đó user yêu cầu cắt LTI theo 2 ngưỡng → sinh các file mới trong `step_4/output/`:
  - `prediction_test_has_default_cut_lti_0_0653_0_1907.csv` (**1,422 dòng, giữ toàn bộ** — FN có 0.0653 ≤ LTI ≤ 0.1907 thành TP: TP sau = 1,314 / FN còn lại 108) + `..._fn_lti_0_0653_0_1907_cut.csv` (449 dòng). *(file bản cũ điều kiện `lti_0_1603` vẫn còn trong output theo task 77)*.
  - `prediction_test_non_default_cut_lti_0_1987_0_342.csv` (**5,092 dòng, giữ toàn bộ** — FP có 0.1987 ≤ LTI ≤ 0.342 thành TN: TN sau = 4,861 / FP còn lại 231) + `..._fp_lti_0_1987_0_342_cut.csv` (1,157 dòng). *(đính chính task 81 — file bản `prob_0_1987_0_342` và `lti_0_221` cũ vẫn còn trong output)*.
  - **Không có bảng DB output** (CSV không import do `.gitignore`/chưa yêu cầu).
- **Lưu model**: `repo_source/db_save_model.py`
  - Chỉ lưu bảng `step_2_model` (baseline, model.id=1) + `step_2_model_coef` (8 hệ số).
  - Bảng `step_4_model` (LogisticRegression 23 biến) **đã bỏ** — không còn mô hình lõi 23 biến theo quyết định user.
- **Tiền xử lý**: bước 2 huấn luyện model 8 biến theo cấu hình `preprocessing` trong `metadata.json`.

## Phiên bản & Commit đang chạy

| Thành phần | Phiên bản | Mô tả |
|---|---|---|
| Python | 3.14.7 | Ngôn ngữ chính (môi trường ảo venv) |
| pandas | 3.0.5 | Xử lý dữ liệu |
| scikit-learn | 1.9.1 | StandardScaler, LogisticRegression |
| Commit | `8719740` | Chuyển file LaTeX cv_tran_ngoc_duc sang file Word (.docx) chuẩn typography và bố cục |

## Kiến trúc Luồng Pipeline

### 1. Luồng chính (Production Pipeline) — Mặc định khi chạy `python run_pipeline.py`
> *Tên gọi nghiệp vụ: Bước 1 → Bước 2 → Bước 3 → Bước 4. Mô hình lõi 23 biến đã bỏ hẳn; Bước 4 = Risk Adjustment áp trên nền baseline.*
```
Bước 1 (Tiền xử lý & Split Train/Test — `step_1`)
   │
   ▼
Bước 2 (`step_2`) — Baseline LogisticRegression 8 biến
   │ (Train Acc ~69.34%, AUC ~0.7274)
   ▼
Bước 3 (`step_3`) — Dự đoán baseline & tách theo target
   │ (Test Acc ~70.14%: non_default 5,092 / has_default 1,422)
   ▼
Bước 4 (`step_4`) — Risk Adjustment: áp bộ luật GỠ/VỚT theo LTI trên nền dự đoán Bước 3
   │ (Accuracy: 70.14% -> 94.80% [sau cắt LTI], TP 1,314 / FP 231 / TN 4,861 / FN 108)
   ▼
Kết quả phê duyệt tín dụng tối ưu và minh bạch toàn hệ thống
```

### 2. Chạy riêng từng phần (`python run_pipeline.py --benchmark-only`)
- `step_2` + `step_3`: chạy riêng baseline 8 biến (tập con của luồng chính).
- Cờ `--all` giữ tương thích, tương đương luồng chính 1→2→3→4.

## Danh sách các bước trong repo:

| Bước | Thư mục | Vai trò | Input | Output |
|---|---|---|---|---|
| **step_1** | `repo_source/step_1/` | **Luồng chính** (Tiền xử lý) | `input/*.xlsx` | `train.csv`, `test.csv`, `label_encoders.json` |
| **step_2** | `repo_source/step_2/` | **Luồng chính** (Baseline 8 biến) | `input/train.csv` | `train_final.csv`, `model.pkl`, `metadata.json` |
| **step_3** | `repo_source/step_3/` | **Luồng chính** (Dự đoán baseline) | model baseline + csv | `prediction_*.csv`, `*_final.csv` |
| **step_4** | `repo_source/step_4/` | **Luồng chính** (Risk Adjustment GỠ/VỚT trên nền baseline; bỏ hẳn mô hình 23 biến) — **đã xóa mọi file, chỉ giữ `input/`** (2 file split từ step_3 + `test.csv` từ step_1) theo yêu cầu user 2026-09-21 | `input/` (test.csv, prediction_test_has_default.csv, prediction_test_non_default.csv) | *(không còn — đã xóa)* |

> Các bước `step_4_1`, `step_4_2` (cũ), `step_5_1`, `step_5_2`, `step_5_3`, `step_5_4` (cũ) và `step_5` đã được xóa khỏi repo (xem lịch sử git nếu cần số liệu benchmark cũ).

### Power BI Semantic Model (`Phân tích nợ xấu.pbix`)
- **Kết nối**: trước đây dùng script `repo_source/step_4/sync_to_power_bi.py` (tự dò port qua `msmdsrv.port.txt` và database qua DMV `$SYSTEM.DBSCHEMA_CATALOGS`). Script **đã bị xóa** cùng toàn bộ file step_4 tại commit `da5fea5` — hiện không còn công cụ đồng bộ PBI trong repo.
- **Trạng thái đồng bộ**: PBI đã đồng bộ đầy đủ luồng 4 bước **2026-09-21** (Số liệu chính + Đóng góp của biến, xem mục 1 — cập nhật task 90).
- Bảng `Mô hình- Số liệu chính`: đã cập nhật số liệu mới (Source TEST): TP **1,314**, FP **231**, FN **108**, TN **4,861**, Recall 0.9241, Precision 0.8505, Accuracy 94.80%.
- Bảng `Danh sách biến mô hình` + `Mô hình - Đóng góp của biến`: hiện đã **đồng nhất 8 biến baseline** — bảng Danh sách biến = DATATABLE 8 dòng; bảng Đóng góp chỉ còn 8 cột, M-expression trỏ file `dong_gop_cua_bien_8.csv` trong repo (xem mục 1 bên dưới, cập nhật 2026-09-21 task 85).

### Dataset đang dùng

- **File**: `repo_source/step_1/input/Credit Risk Dataset Chính.xlsx`
- **Dung lượng**: 32,566 dòng × 29 cột, 3 sheets
- **Sheet dữ liệu**: "Dữ liệu rủi ro tín dụng"
- **Target**: `Trạng thái trả nợ (0 = không vỡ nợ, 1 = vỡ nợ)` — 25,459/7,107
- **Categorical**: 11 cột → Label Encoding (lưu `label_encoders.json`)
- **Giữ cột ID**: `Mã khách hàng` (không drop, exclude khỏi label encoding)
- **Split**: train 26,052 / test 6,514 (80/20, stratify)

### Kết quả luồng hiện tại (baseline 8 biến + cắt LTI tại step_4)

- **Baseline (Bước 2/3)**: Train Acc ~69.34%, AUC ~0.7274; Test Acc ~70.14% (TP 865 / FP 1,388 / TN 3,704 / FN 557).
- **Risk Adjustment (Bước 4)** — cắt FN/FP theo LTI (ngưỡng task 82):
  - has_default: FN có 0.0653 ≤ LTI ≤ 0.1907 → TP (449/557 FN bắt lại).
  - non_default: FP có 0.1987 ≤ LTI ≤ 0.342 → TN (1,157/1,388 FP chuyển).
  - Kết quả sau cắt (chạy `metrics_after_cut.py`): TP 1,314 / FP 231 / TN 4,861 / FN 108 → Acc 0.9480 | Precision 0.8505 | Recall 0.9241 | F1 0.8857 | Specificity 0.9546.
- **Lưu ý**: Ngưỡng cắt LTI và số liệu sau cắt được chốt theo model 8 biến hiện hành.

# Hiện trạng hệ thống

## 1. Power BI (Desktop local, port 57230)
- Mô hình "Phân tích nợ xấu" — database id `16892c19...`; bảng **Mô hình- Số liệu chính** cập nhật số liệu TEST mới nhất (2026-09-21): TP 1,314 / FP 231 / FN 108 / TN 4,861; Accuracy 0.9480; Recall 0.9241; Precision 0.8505; F1 0.8857; Specificity 0.9546; FPR 0.0454; FNR 0.0759; ROC AUC 0.8593; PR AUC 0.745; KS 0.585; Brier 0.101; Log Loss 0.335; Threshold 0.5.
- Partition `Mô hình- Số liệu chính` (kiểu M) đọc từ file CSV trong repo: `C:\Users\This PC\Desktop\179\repo_source\step_4\output\so_lieu_chinh_test.csv` (không còn trỏ file ngoài repo).
- **Bảng biến + đóng góp (theo mô hình 8 biến, task 85, `a4c09c1`)**: bảng `Danh sách biến mô hình` = DATATABLE calculated 8 dòng (STT 1–8: Lãi suất, LTI, DTI tổng, Thu nhập hàng năm, Tình trạng sở hữu nhà, Từng vỡ nợ, Số tiền vay đề nghị, Mục đích khoản vay); bảng `Mô hình - Đóng góp của biến` chỉ còn **8 cột** (đã xóa 15 cột biến cũ), M-expression đọc `C:\Users\This PC\Desktop\179\repo_source\step_4\output\dong_gop_cua_bien_8.csv`.
- **Đóng góp 8 biến (%) tính bằng |coef| × std(feature) theo module `repo_source/step_4/compute_contribution.py`**: Tỷ lệ khoản vay trên thu nhập 38.28; Lãi suất 28.16; Số tiền vay 20.43; Thu nhập 4.44; Sở hữu nhà 3.04; Từng vỡ nợ 2.77; DTI 2.44; Mục đích 0.43.

## Ghi chú
- Cập nhật file này mỗi khi deploy thay đổi hệ thống (server, service, schema, route...).

### Chỉ số mô hình sau khi cắt LTI (tasks 80 + 82, cập nhật 2026-09-21, commit `9110c67`)
- Baseline cũ (Bước 3): Acc ~70.14% (TP 865 / FP 1,388 / TN 3,704 / FN 557).
- Điều chỉnh: has_default FN có 0.0653 ≤ LTI ≤ 0.1907 → TP (449 ca); non_default FP có 0.1987 ≤ LTI ≤ 0.342 → TN (1,157 ca).
- Kết quả toàn hệ thống: **TP 1,314 / FP 231 / TN 4,861 / FN 108** → **Accuracy 94.80%** | Precision 85.05% | Recall 92.41% | F1 88.57% | Specificity 95.46%.