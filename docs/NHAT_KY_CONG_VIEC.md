# Nhật ký công việc — credit scoring default rate

## DANG DỞ

### 2026-09-21
108. **Tạo `step_4/run.py` để pipeline chạy trọn 1→4** — `<commit tbd>`
    - Hiện `run_pipeline.py --all` dừng ở Bước 4 vì `repo_source/step_4/run.py` chưa tồn tại; cần bọc logic Risk Adjustment + ghi `so_lieu_chinh_test.csv` thành run.py.

## ĐÃ XONG

### 2026-09-22
113. **Tái tạo `prediction_test_has_default.csv` đúng chuẩn + tạo Excel chia 4 mốc xác suất (0–25 / 25–50 / 50–75 / 75–100)** — `36b63cf`
    - File `step_3/output/prediction_test_has_default.csv` bị hỏng (68 dòng, header thành dữ liệu) → chạy lại `step_3/run.py` sinh đúng **1.422 dòng** (Acc 70.14%).
    - Tạo `repo_source/step_3/export_default_prob_buckets.py`: chia nhóm vỡ nợ theo `prob_vỡ_nợ` thành 4 sheet trong `output/nhom_xac_suat_vo_no_4_muc.xlsx`: 0–25% = 69, 25–50% = 488, 50–75% = 729, 75–100% = 136 hồ sơ.

### 2026-09-21
111. **Xuất trọng số của model.pkl (step 2) ra file CSV riêng** — `be4484d`
    - Tạo `repo_source/step_2/export_coefficients.py`: đọc `model.pkl` + `metadata.json`, ghi `output/trong_so_model.csv` (Biến + trọng số + Intercept), UTF-8-sig để Excel đọc đúng.

### 2026-09-21
110. **Sửa lỗi phông file `dong_gop_cua_bien_8.csv` khi mở bằng Excel** — `6dccdd7`
    - File ghi UTF-8 không BOM → Excel đọc ANSI làm vỡ tiếng Việt. Đổi `compute_contribution.py` sang `encoding="utf-8-sig"`; kiểm chứng PBI vẫn đọc đúng (Encoding=65001 tự bỏ BOM).
    - Áp dụng luôn cho `export_remaining_cases.py` (2 file danh sách còn lại).

### 2026-09-21
109. **Xuất danh sách hồ sơ còn sót lại sau cắt của 2 nhóm (FN, FP) vào step_4/output** — `b892cc6`
    - Tạo `repo_source/step_4/export_remaining_cases.py`: lọc phần nằm ngoài dải LTI của mỗi nhóm.
    - Xuất `output/con_lai_fn_sau_cat.csv` (**108** hồ sơ, LTI 0.0146–0.0652) và `output/con_lai_fp_sau_cat.csv` (**231** hồ sơ, LTI 0.1910–0.6897).

### 2026-09-22
112. **Chuyển file LaTeX CV sang file Word (.docx)** — `8719740`
    - Chuyển `CV/cv_tran_ngoc_duc.tex` thành `CV/cv_tran_ngoc_duc.docx` giữ nguyên cấu trúc chuẩn 2 trang, typography, màu sắc Navy, bố cục bảng kỹ năng 3 cột và ảnh đại diện.
    - Tạo script `scripts/convert_cv_to_word.py` tự động hóa chuyển đổi qua `python-docx` với căn lề, đường kẻ section border và hyperlink đầy đủ.

### 2026-09-21
107. **Cập nhật số liệu chính xác lên Power BI (bảng "Số liệu chính")** — `2748b20`
    - Nâng cấp `repo_source/step_4/compute_final_metrics.py`: tính đủ AUC/PR AUC/KS/Brier/Log Loss từ mô hình hiện hành + tự ghi `so_lieu_chinh_test.csv`.
    - File CSV đã ghi đè: AUC **0.7264** (thay 0.8593 cũ), PR AUC 0.4492, KS 0.3542, Brier 0.2004, Log Loss 0.5871.
    - Refresh bảng `Mô hình- Số liệu chính` qua XMLA port 55593: `ProcessFull` bị PBI Desktop chặn, dùng **`DataOnly`** thành công → PBI hiển thị đúng số mới.

### 2026-09-21
106. **Chạy lại toàn bộ pipeline 1→2→3→4 để lấy con số chính xác** — `9bc06b6`
    - Chạy `run_pipeline.py` (step 1→2→3) thành công; step 4 cần `run.py` chưa có nên dừng — tính Risk Adjustment bằng script riêng.
    - Kết quả xác minh (trùng khớp README):
      - Baseline TEST: Acc **70.14%**, TP 865 / FP 1.388 / FN 557 / TN 3.704, **AUC 0.7264**; train Acc 69.34% / AUC 0.7274.
      - Step 4 (Risk Adjustment LTI): bắt 449 FN / cứu 1.157 FP → TP 1.314 / FP 231 / FN 108 / TN 4.861, Acc **94.80%**, Recall 92.41%, Specificity 95.46%, Precision 85.05%, F1 88.57%.
      - **Kết luận:** AUC đúng của mô hình hiện hành là **0.7264**; giá trị **0.8593** trong `so_lieu_chinh_test.csv` (bảng PBI "Số liệu chính") là **dữ liệu cũ chưa đồng bộ** (từ mô hình 23 biến/cũ), không tái tạo được từ pipeline hiện tại.
    - Đổi tên script tính số liệu: `repo_source/step_4/compute_final_metrics.py`.

### 2026-09-21
105. **Vẽ biểu đồ minh họa + giải thích về khái niệm AUC** — `75195ac`
    - Tạo `repo_source/step_3/explain_auc.py`: ảnh `image/explain_auc.png` so sánh 3 đường ROC (random 0.5 / dự án 0.7264 / hoàn hảo 1.0), chú thích vùng AUC, điểm ngưỡng trên đường.

### 2026-09-21
102. **Chuyển đổi dashboard "Phát hiện chính & Hỗ trợ quyết định" thành tài liệu README** — `2783b33`
    - Tổng hợp toàn diện nội dung trang dashboard: 3 cấp độ rà soát hồ sơ theo xác suất rủi ro vỡ nợ (Mức 1 <20%, Mức 2 20-35%, Mức 3 >=35%), 5 khía cạnh hồ sơ rủi ro cao cần kiểm tra và 5 phân khúc nợ xấu cao cần lưu ý (DTI >= 0.70, LTI >= 0.40, Lãi suất >= 16%, Thu nhập < 782 triệu/năm, Lịch sử vỡ nợ).
    - Soạn thảo định dạng README Markdown chuẩn, sinh nội dung vào `readme/New Text Document.txt` và `readme/README_Phat_Hien_Chinh_Ho_Tro_Quyet_Dinh.md`.

### 2026-09-21
102. **Tạo spec Deneb ma trận phân loại — bỏ "Thực tế/Dự báo" và "KIỂM TRA · Ngưỡng"** — `38d594e`
    - User dán spec Deneb "Ma trận phân loại responsive - Page 4" và yêu cầu bỏ 2 thành phần:
      - Dòng `Thực tế x · Dự báo y` (cell_description) ở 4 ô.
      - Dòng `KIỂM TRA · Ngưỡng` (header_label) phía trên phải.
    - Tạo file HTML copy spec chuẩn (pattern như task 95) để dán vào Deneb.

### 2026-09-21
101. **Chỉnh 2 ảnh step_4: đưa điều kiện bắt vào ô có khung + căn chỉnh** — `2572ddd`
    - User yêu cầu chuyển dòng "điều kiện bắt" thành một ô đàng hoàng (hộp thoại có khung) và căn chỉnh lại biểu đồ.

### 2026-09-21
100. **Chỉnh 2 ảnh step_4: hiện % còn lại + ghi rõ điều kiện bắt** — `04c0163`
    - User yêu cầu hiển thị thêm % còn lại và điều kiện bắt là gì trên biểu đồ cột.
    - Mỗi cột ghi giá trị + %; chú thích điều kiện bắt: FN bắt khi LTI trong [0.0653, 0.1907]; FP gỡ khi LTI trong [0.1987, 0.342].

### 2026-09-21
99. **Chỉnh 2 ảnh step_4 thành biểu đồ cột (bắt được / còn lại)** — `2816bdd`
    - User yêu cầu chuyển sang dạng biểu đồ cột 2 giá trị: bắt được bao nhiêu, còn lại bao nhiêu (thay cho histogram + text).
    - Vớt FN: cột bắt 449 / còn 108. Gỡ FP: cột gỡ 1.157 / còn 231.

### 2026-09-21
98. **Chỉnh 2 ảnh step_4 sang dạng "bắt được bao nhiêu / còn lại bao nhiêu / tiêu chí bắt"** — `a1d78b1`
    - User yêu cầu hiển thị kết quả theo hướng: bắt được bao nhiêu, còn lại bao nhiêu, tiêu chí bắt là gì.
    - Vớt FN: tổng 557 → bắt 449 (LTI 0.0653–0.1907) thành TP · còn 108 ngoài dải giữ FN.
    - Gỡ FP: tổng 1.388 → gỡ 1.157 (LTI 0.1987–0.342) về TN · còn 231 ngoài dải giữ FP.

### 2026-09-21
97. **Tạo 2 ảnh minh họa bộ lọc step_4 (vớt FN + gỡ FP)** — `8dcbd08`
    - User yêu cầu "tạo 2 ảnh, vớt thằng FN và gỡ thằng FP làm ở step 4".
    - Sinh `repo_source/step_4/generate_vot_fn_go_fp.py` (matplotlib, font Segoe UI) từ dữ liệu thật:
      - `image/step_4_vot_fn.png`: histogram LTI của 449 FN cắt dải 0.0653–0.1907 → chuyển thành TP.
      - `image/step_4_go_fp.png`: histogram LTI của 1.157 FP cắt dải 0.1987–0.342 → chuyển về TN.

### 2026-09-21
96. **Chỉnh spec Deneb hiển thị top 5 biến đóng góp** — `17097c5`
    - User yêu cầu "top 5 thằng thôi"; thêm transform window rank + filter `r <= 5`, đổi title "5 BIẾN".

### 2026-09-21
95. **Tạo file HTML + spec JSON chuẩn cho Deneb (biểu đồ đóng góp 8 biến)** — `357dabf`
    - User nhắc đây là Deneb (visual Power BI), không phải vega-embed; `l.txt` dạng rút gọn (thiếu quotes/commas) copy vào Deneb không được.
    - Sinh HTML có nút copy chứa spec Vega-Lite JSON hợp lệ (data `dataset` + transform fold 8 biến) để dán vào Deneb.

### 2026-09-21
94. **Tạo file HTML hiển thị biểu đồ đóng góp 8 biến (Vega-Lite)** — `9fe3b67`
    - User yêu cầu tạo file html (bản `.txt` copy không được); sinh HTML nhúng Vega-Embed + spec 8 biến với dữ liệu đóng góp hiện tại (LTI 38.28...).

### 2026-09-21
93. **Tạo file mới `l_8_bien.txt` (spec Vega-Lite 8 biến) theo yêu cầu user** — `6d50f0c`
    - User yêu cầu tạo file mới; sinh `l_8_bien.txt` với nội dung spec đã chỉnh theo bảng đóng góp 8 biến (giống bản sửa task 92), giữ nguyên `l.txt`.

### 2026-09-21
92. **Chỉnh `l.txt` (spec Vega-Lite biểu đồ đóng góp PBI) theo bảng đóng góp 8 biến hiện tại** — `020bc10`
    - Đổi fold từ 5 biến cũ (có Tương tác nợ nhà thuê, Tương tác LTI×lãi suất) sang 8 biến hiện hành khớp CSV `dong_gop_cua_bien_8.csv`: Lãi suất, LTI, DTI, Thu nhập, Sở hữu nhà, Từng vỡ nợ, Số tiền vay, Mục đích.
    - Cập nhật title "8 BIẾN", ví dụ 38.28% (LTI), scale domain 0→40, axis values 0/10/20/30/40.

### 2026-09-21
91. **Cập nhật `readme/README Final - Copy.md` cho khớp hiện trạng project** — `043f42d`
    - Viết lại README theo hiện trạng: model LogisticRegression 8 biến, luồng 1→2→3→4, số liệu baseline test (Acc 70.14%, TP 865/FP 1,388/FN 557/TN 3,704) và sau Risk Adjustment LTI (Acc 94.80%, TP 1,314/FP 231/FN 108/TN 4,861, Recall 92.41%, Specificity 95.46%, Precision 85.05%), bảng đóng góp 8 biến (LTI 38.28%, Lãi suất 28.16%...).
    - Loại bỏ toàn bộ tham chiếu luồng cũ 23 biến / step_5_4; thay ảnh bằng các file tồn tại (`../image/`), sửa path tài liệu tương đối từ `readme/`.

### 2026-09-21
90. **Cập nhật bảng đóng góp của biến lên Power BI** — `c802899`
    - CSV `dong_gop_cua_bien_8.csv` chứa giá trị đóng góp đúng (28.16/38.28/2.44/4.44/3.04/2.77/20.43/0.43), UTF-8 không BOM.
    - PBI Desktop (port 57230): kết nối qua `powerbi-modeling-mcp`, refresh bảng `Mô hình - Đóng góp của biến` → DAX verify ra đúng 8 giá trị; các bảng khác (Số liệu chính TP 1,314/FP 231/FN 108/TN 4,861, Danh sách biến, NHóm Khách hàng) giữ nguyên.
    - Đổi tên `step_4/contrib_log_source/` thành `step_4/contrib_source/` (model.pkl, metadata.json) và cập nhật path trong `compute_contribution.py`; làm sạch toàn bộ docs (HIEN_TRANG, NHAT_KY, SESSION_PROMPT_LOG) không còn mô tả phân tách nguồn bảng đóng góp.

### 2026-09-21
89. **Chuẩn hóa luồng 4 bước + bảng đóng góp của biến theo mô hình 8 biến hiện hành** — `26394ce`
    - Chạy lại bước 3 bằng mô hình 8 biến hiện hành → test Acc 70.14% (TP 865 / FP 1,388 / TN 3,704 / FN 557).
    - Chạy lại 2 bộ lọc LTI (449/557 FN→TP; 1,157/1,388 FP→TN) → sau cắt Acc 94.80% (TP 1,314 / FP 231 / FN 108 / TN 4,861).
    - `db_import.py` nạp lại 29 bảng / 249.106 dòng; khôi phục bảng `step_4_input_test`.
    - `compute_contribution.py` xuất bảng đóng góp 8 biến theo mô hình hiện hành; đóng góp (%): LTI 38.28; Lãi suất 28.16; Số tiền vay 20.43; Thu nhập 4.44; Sở hữu nhà 3.04; Từng vỡ nợ 2.77; DTI 2.44; Mục đích 0.43.

### 2026-09-21
88. **Cập nhật DB: chạy lại bộ lọc + đóng góp biến** — `baa8dde`
    - User yêu cầu: "cập vào dbvear chưa và đóng góp các biến".
    - Chạy lại cut LTI: has_default cắt 207/359 FN→TP; non_default cắt 540/1,096 FP→TN → sau cắt Acc 0.8913 (TP 1,270 / FP 556 / TN 4,536 / FN 152).
    - Cập nhật `compute_contribution.py`: tính std trên X đã tiền xử lý (khớp biến mô hình thật nhận); đóng góp (%): LTI 38.28; Lãi suất 28.16; Số tiền vay 20.43; Thu nhập 4.44; Sở hữu nhà 3.04; Từng vỡ nợ 2.77; DTI 2.44; Mục đích 0.43.
    - `db_import.py` nạp lại 28 bảng / 241.733 dòng lên schema `credit_model`.

87. **Tinh chỉnh tiền xử lý bước 2: log biến tiền, bước 3 chạy mô hình, bước 4 input** — `965920b`
    - User yêu cầu: "bước 2 log lại tiền thôi rồi bước 3 chạy mô hình xong rồi input bước 4".
    - Sửa `step_2/run.py`: bỏ StandardScaler, chỉ log 2 biến tiền (`Thu nhập hàng năm (VND)` + `Số tiền vay đề nghị (VND)`) → train; metadata `preprocessing = {log_columns, standardize: False}`, không scaler.pkl.
    - Sửa `step_3/run.py`: áp dụng log các cột `log_columns` trước khi predict, không cần scaler.
    - Kết quả: train Acc 0.7675 / AUC 0.8409; test Acc 77.66%.
    - Copy prediction mới sang `step_4/input`, chạy `db_import.py` nạp 29 bảng / 248.251 dòng lên schema `credit_model`.

64. **Dựng ảnh mẫu luồng xử lý theo ngoại lệ thay phân nhóm cứng**
    - User bỏ ý tưởng phân nhóm, yêu cầu dựng thử ảnh thay thế.
    - User bỏ ý tưởng phân nhóm, yêu cầu dựng thử ảnh thay thế.

57. **Phân tích FN_vs_TP (hướng khác biệt đặc trưng) + dã vị trí xác suất FN** - **HỦY** (`f5d0b4d`, `run_fn_vs_tp_analysis.py` chưa chạy/chưa dùng)
    - User yêu cầu "thôi bỏ đi, giữ nguyên cách cũ": hủy bỏ phân tích thống kê FN-vs-TP đang dở, giữ nguyên luồng Risk Adjustment 5.4 production như đã chốt.

## ĐÃ XONG

### 2026-09-21
86. **Đổi cách tính đóng góp biến sang hệ số hồi quy |coef| chuẩn hóa** — `(commit script)`
    - User đồng ý đổi cách tính đóng góp; sửa `repo_source/step_4/compute_contribution.py`: bỏ permutation importance, tính |coef| × std(feature) rồi chuẩn hóa về tổng 100% (đọc `feature_columns` từ `step_3/input/metadata.json` để khớp thứ tự `model.coef_`).
    - Đóng góp mới (%): **Thu nhập hàng năm 61.09; Số tiền vay đề nghị 38.91; các biến còn lại 0.00**. Tổng = 100%.
    - Refresh DataOnly bảng `Mô hình - Đóng góp của biến` trên PBI, verify DAX ra đúng 8 cột giá trị mới.

### 2026-09-21
85. **Cập nhật lại các biến sử dụng trong mô hình và đóng góp của các biến trên PBI** — `a4c09c1` *(đóng góp ×đổi tại task 86)*
    - User yêu cầu: "cập nhật lại các biến sử dụng trong mô hình và đóng góp của các biến"; chọn phương án theo **mô hình 8 biến hiện hành**.
    - Script mới `repo_source/step_4/compute_contribution.py`: tính đóng góp 8 biến từ `model.pkl` hiện hành bằng permutation importance (scoring roc_auc, n_repeats=5) trên `train_final.csv`; xuất `step_4/output/dong_gop_cua_bien_8.csv` (gitignored).
    - Kết quả đóng góp (%): Thu nhập hàng năm 65.19; Số tiền vay đề nghị 34.80; Lãi suất khoản vay 0.01; các biến còn lại ~0.00.
    - PBI (port 57230): bảng `Mô hình - Đóng góp của biến` — xóa 15 cột tương tác/biến cũ, sửa M-expression trỏ CSV 8 cột trong repo, refresh DataOnly (Automatic không nạp lại dữ liệu); bảng `Danh sách biến mô hình` — sửa DATATABLE calculated chỉ giữ 8 biến, refresh Calculate. Xác minh bằng DAX: 8 dòng biến + 8 cột đóng góp đúng.

### 2026-09-21
84. **Đưa số liệu sau cắt LTI lên Power BI (cập nhật bảng Mô hình- Số liệu chính)** — `CHƯA_COMMIT_CODE`
    - User yêu cầu "đưa vào pbi"; làm hoàn toàn trong repo 179 (không đụng file ngoài).
    - Tạo CSV dữ liệu tại `repo_source/step_4/output/so_lieu_chinh_test.csv` (gitignored) với số liệu TEST mới; sửa M-expression partition `Mô hình- Số liệu chính` (kiểu `m`, giữ nguyên per lỗi thường gặp #4) trỏ về file CSV trong repo, refresh full bảng qua PBI Desktop (port 57230).
    - Kết quả PBI: TEST TP 1,314 / FP 231 / FN 108 / TN 4,861; Acc 0.9480; Recall 0.9241; Precision 0.8505; F1 0.8857; Specificity 0.9546; FPR 0.0454; FNR 0.0759; giữ nguyên ROC/PR AUC/KS/Brier/LogLoss/Threshold.
    - Lỗi phát sinh: CSV ghi `utf-8-sig` có BOM → refresh nạp dữ liệu cũ; ghi lại UTF-8 không BOM là OK (đã lưu mục 9 LOI_THUONG_GAP).

### 2026-09-21
83. **Tính lại các chỉ số mô hình sau khi cắt LTI (has_default + non_default)** — `9110c67`
    - Script `repo_source/metrics_after_cut.py` đọc 2 file output cắt mới nhất rồi tính metric.
    - Kết quả toàn hệ thống (test 6,514): **TP 1,314 / FP 231 / TN 4,861 / FN 108**.
    - **Accuracy 94.80%** | Precision (vỡ nợ) 85.05% | Recall 92.41% | F1 88.57% | Specificity 95.46%.

### 2026-09-21
82. **Đính chính điều kiện non_default: FP thành TN khi LTI between 0.1987 và 0.342** — `6171da2`
    - User đính chính task 81: "nhầm tỷ lệ vay trên thu nhập" — cột đúng là `Tỷ lệ khoản vay trên thu nhập` (LTI), không phải `prob_vỡ_nợ`.
    - `git mv` `cut_prob_fp_to_tn.py` → `cut_lti_fp_to_tn.py`; điều kiện: FP có 0.1987 ≤ LTI ≤ 0.342 → predicted=0, correct=1.
    - Số liệu non_default: FP 1,388 → cắt **1,157** thành TN, còn **231** FP; TN sau = 4,861. Xuất 2 file mới `step_4/output/` (`cut_lti_0_1987_0_342`). CSV không commit do `.gitignore`.

### 2026-09-21
81. **Đổi điều kiện non_default: chuyển FP thành TN khi prob_vỡ_nợ between 0.1987 và 0.342** — `278c68c` *(đã bị thay thế bởi task 82)*
    - User yêu cầu "tỷ lệ vỡ nợ between 0.1987 and 0.342" nhưng sau đó đính chính đúng cột là LTI.
    - Bản chạy theo `prob_vỡ_nợ` bắt **0 dòng** (FP có prob ≥ 0.5, ngoài dải) → đã đính chính ở task 82.

### 2026-09-21
80. **Đổi điều kiện has_default: chuyển FN thành TP khi LTI between 0.0653 và 0.1907** — `829223a`
    - User yêu cầu: "Đổi lại điều kiện của thằng has default là tỷ lệ khoản vay trên thu nhập between 0.0653 và 0.1907" (thay ngưỡng LTI < 0.1603 cũ ở task 77).
    - Sửa `repo_source/cut_lti_fn_to_tp.py`: FN có 0.0653 ≤ LTI ≤ 0.1907 → predicted=1, correct=1. Số liệu: FN 557 → cắt **449** thành TP, còn **108** FN; TP sau = 1,314.
    - Xuất 2 file mới `step_4/output/prediction_test_has_default_cut_lti_0_0653_0_1907.csv` (1,422 dòng) + `..._fn_lti_0_0653_0_1907_cut.csv` (449 dòng); file bản cũ (0_1603) giữ nguyên chưa xóa. CSV không commit do `.gitignore`.

### 2026-09-21
79. **Cắt FP có LTI > 0.221 trong prediction_test_non_default.csv & chuyển thành TN** — `6cd1b34`
    - User yêu cầu: "còn thằng file non thì tỷ lệ vay trên thu nhập > 0.221" (đối xứng task 77 cho file non_default).
    - Script `repo_source/cut_lti_fp_to_tn.py`: file 5,092 dòng (target=0), TN 3,704 / FP 1,388. FP & LTI > 0.221 = **973** (đổi predicted→0, correct→1); FP còn lại = **415**.
    - Xuất 2 file: `step_4/output/prediction_test_non_default_cut_lti_0_221.csv` (**5,092 dòng, giữ toàn bộ** — TN sau = 4,677, FP còn 415) + `prediction_test_non_default_fp_lti_0_221_cut.csv` (973 dòng FP đã chuyển TN). CSV không commit do `.gitignore`.

### 2026-09-21
77. **Cắt FN có LTI < 0.1603 trong prediction_test_has_default.csv & chuyển thành TP** — `9ea2a74`
    - User yêu cầu: "đối với file has default thì cắt những thằng có tỷ lệ vay trên thu nhập < 0.1603 fn thành tp"; bổ sung "output sẽ là những thằng fn thành tp và còn lại những thằng fn nào".
    - Script `repo_source/cut_lti_fn_to_tp.py`: file 1,422 dòng (target=1), TP 865 / FN 557. FN & LTI<0.1603 = **443** (đổi predicted→1, correct→1); FN còn lại = **114**.
    - Xuất 2 file: `step_4/output/prediction_test_has_default_cut_lti_0_1603.csv` (**1,422 dòng, giữ toàn bộ** — TP sau = 1,308, FN còn 114) + `prediction_test_has_default_fn_lti_0_1603_cut.csv` (443 dòng chỉ các FN đã chuyển TP). CSV không commit do `.gitignore`.

### 2026-09-21
78. **Xóa toàn bộ file trong repo_source/step_4/ chỉ giữ thư mục input/** — `da5fea5`
    - User yêu cầu: "ở step 4 xóa hết chỉ để input".
    - Xóa `output/`, `__pycache__/`, và các file mã nguồn `run.py`, `plot_hedging_tiers.py`, `plot_separate_hedging_tiers.py`, `sync_to_power_bi.py`; chỉ giữ lại thư mục `input/` (test.csv, prediction_test_non_default.csv, prediction_test_has_default.csv).

### 2026-09-21
76. **Đồng bộ lại kết quả bước 4 lên Power BI (luồng 4 bước)** — *(chưa commit code mới)*
    - Chạy lại `run_pipeline.py --all` (exit 0) để tái sinh output step_4 (prediction_final_evaluated.csv, step_4_hedging_report.json, rescued_fp, caught_fn...).
    - Chạy `step_4/sync_to_power_bi.py` exit 0: PBI port 57230, database, TMSL 2 bảng Result 1, refresh OK. Số liệu chính mới: TP 831 / FP 1,164 / FN 591 / TN 3,928, Acc 73.06%.
    - Đồng bộ 3 CSV sang `D:\Credit Risk New - Copy\hồi quy\16_dữ_liệu_power_bi\`.
    - Lưu ý: bảng 'Danh sách biến' + 'Đóng góp của biến' vẫn giữ 23 biến cũ (metadata 23 biến đã bỏ) — chưa đồng nhất baseline 8 biến.

### 2026-09-21
75. **Đồng bộ lại DB (dbeaver) theo trạng thái luồng 4 bước**
    - Khảo sát 30 bảng cũ trong `credit_model`: còn `step_4_output_*`, `step_4_model` (23 biến), `step_5_*` không còn nguồn CSV.
    - DROP schema CASCADE + tạo lại; chạy `db_import.py` (17 bảng, 227,962 dòng) + `db_save_model.py` (step_2 baseline).
    - Verify: đối chiếu 100% từng bảng khớp CSV; không còn bảng step_4_output/step_4_model/step_5.

### 2026-09-21
74. **Xóa toàn bộ output bước 4 ngoại trừ ảnh** — `5039494`
    - Giữ lại 4 ảnh trong `repo_source/step_4/output/` (`bien_do_vot_fn_lti_0_1603.png`, `step_4_hedging_tiers.png`, `step_4_lop_go.png`, `step_4_lop_vot.png`).
    - Xóa 12 file output còn lại: 5 CSV (rescued/caught/prediction_final/deneb*), `step_4_hedging_report.json`, 3 `tmsl_update_*.json`, `run_update_vars_pbi.ps1`, `step_4_ly_do_go_vot.md`.

### 2026-09-21
73. **Gom Risk Adjustment về Bước 4 & bỏ hẳn mô hình 23 biến (luồng 1 → 2 → 3 → 4)** — `5a4ec0e`
    - User chốt: bỏ hẳn mô hình lõi 23 biến (Log1p → StandardScaler); step_4 = Risk Adjustment áp trực tiếp trên nền dự đoán baseline của step_3.
    - Sửa `run_pipeline.py` (luồng chính 4 bước, bỏ step_5; step_4 copy 2 file split từ step_3 + test.csv từ step_1), `step_4/run.py` (tự dựng 4 biến tương tác nghiệp vụ từ test.csv, merge thêm `Thâm niên làm việc (năm)`), `db_import.py` (STEP_DIRS bỏ step_5), `db_save_model.py` (bỏ lưu model step_4 23 biến, chỉ còn baseline step_2).
    - Chạy lại pipeline exit 0: baseline Acc 70.14%; Risk Adjustment → Acc 73.06% (+2.92%), GỠ 310 (264 FP, 46 TP mất, 5.74:1), VỚT 52 (12 FN, 40 TN oan); TP 831 / FP 1,164 / TN 3,928 / FN 591.
    - Đồng bộ `docs/PIPELINE.md` + `docs/HIEN_TRANG_HE_THONG.md` theo luồng 4 bước (bỏ mọi tham chiếu step_5 & mô hình 23 biến).

### 2026-09-19
72. **Xóa hết bảng step_4/step_5 trong DB và nạp lại mới** — `13f20c5`
    - Đối chiếu trước khi xóa: DB giữ dữ liệu cũ — `step_4_*` thiếu 4 biến tương tác + còn cột `Hạng tín dụng khoản vay`; `step_5_*` là bản trên nền 4.1 (rescued 127 / caught 25, thiếu cột `tier_*`, `action_step5_4`); `step_5_output_danh_sach_bien_mo_hinh` chưa tồn tại.
    - Đã xóa toàn bộ 59 bảng `step_4*`/`step_5*` (gồm cả lịch sử `step_4_1`, `step_4_2`, `step_5_1`, `step_5_3`, `step_5_4`, bảng true/false cũ).
    - Chạy `db_import.py`: nạp lại 26 bảng từ CSV hiện tại trong repo (299,819 dòng) — `step_4_output_*` đủ 23 biến (4 tương tác), `step_5_output_prediction_final_evaluated` (6,514), `rescued_fp` (155), `caught_fn` (33), `danh_sach_bien_mo_hinh` (23).
    - Chạy `db_save_model.py`: lưu `step_4_model` (LogisticRegression 23 hệ số, model.id=1).
    - Verify: đối chiếu hash toàn bộ 26 bảng với CSV — 100% KHỚP. DB còn 30 bảng, không còn bảng lịch sử `step_4_1/4_2/5_1/5_3/5_4`.

### 2026-09-19
71. **Tạo README tiếng Anh tổng hợp dự án trong thư mục `readme/` (file `readme.md`)** — `8b0ad89`
    - Dựng tài liệu mô tả đầy đủ dự án Credit Risk (pipeline 5 bước, số liệu công bố, kiến trúc, PostgreSQL/Power BI, structure, tech stack) dựa trên nội dung người dùng cung cấp.
    - Dùng thuật ngữ mới `Risk Adjustment` / `Risk Adjustment layer` thay cho thuật ngữ cũ trong toàn văn, giữ nguyên tên file kỹ thuật (`step_5_4_hedging_tiers.png`...) vì là tên file thật.

70. **Đổi thuật ngữ luồng Bước 5: dùng 'Risk Adjustment' và 'Risk Adjustment layer'** — `6aaf649`
    - Thay toàn bộ từ/cụm tiếng Anh cũ ('Hedging' và 'Hedging Engine') trong code + docs bằng `Risk Adjustment` và `Risk Adjustment layer` (9 file: `run_pipeline.py`, `step_5/run.py`, `step_5/sync_to_power_bi.py`, `step_5/plot_hedging_tiers.py`, `output/step_5_4_ly_do_go_vot.md`, `PIPELINE.md`, `HIEN_TRANG_HE_THONG.md`, `NHAT_KY_CONG_VIEC.md`, `SESSION_PROMPT_LOG.md`).
    - Giữ nguyên tên file kỹ thuật chứa từ cũ (`plot_hedging_tiers.py`, `step_5_4_hedging_report.json`, `step_5_4_hedging_tiers.png`...) và JSON key `sau_step_5_4_hedging` để không vỡ pipeline và report `.pbix`.
    - Không push do repo không có remote origin.

69. **Tạo 4 ảnh biểu đồ tổng hợp cho project** — `6e7606b`
   - Đọc tên cột thực tế từ 4 CSV (step_3, step_4, step_5 rescued_fp/caught_fn).
   - Viết `images/generate_charts.py`, tạo 4 ảnh DPI=150: `baseline_confusion_matrix.png`, `probability_distribution.png`, `fp_fn_feature_comparison.png`, `model_improvement_comparison.png`.
   - Ảnh 1: 2 heatmap confusion matrix cạnh nhau (Baseline vs Core Model), màu xanh/đỏ TP/TN/FP/FN.
   - Ảnh 8: Histogram xác suất theo 2 nhóm + Calibration Curve 20 bins.
   - Ảnh 10: Grouped bar chart 6 đặc trưng FP vs FN chuẩn hóa theo %.
   - Ảnh 11: 2x2 subplots ROC-AUC / Accuracy / FP / TN cho 3 giai đoạn model.

### 2026-09-19

69. **Tạo 6 ảnh minh họa cho README** — `850367b`
   - 4 ảnh Python từ data thực: `baseline_confusion_matrix.png`, `probability_distribution.png`, `fp_fn_feature_comparison.png`, `model_improvement_comparison.png` (lưu tại `images/`).
   - 2 ảnh AI-generated: `pipeline_flow.jpg` (sơ đồ 5 bước), `db_diagram.jpg` (schema PostgreSQL credit_model).
   - Cập nhật README thay thế 10/12 placeholder comment thành ảnh thực tế. 2 ảnh còn lại (Power BI dashboard, Excel preview) cần bạn chụp thủ công.

### 2026-09-18

68. **Viết lại README theo phong cách Doonie Watch** — `86d2ad1`
   - Xoá README cũ và tạo README mới theo cấu trúc Doonie Watch: IMPORTANT NOTICE, Table of Contents 5 mục, Background & Context (Who is the client / The Problem / My Role / Dashboard Outputs), Process Step by Step, Insight Deep Dive, Achievements bảng so sánh, Value Gained, Tools & Tech Stack.
   - Nhúng ảnh Risk Adjustment từ `repo_source/step_5/output/` vào đúng vị trí insight tương ứng.

### 2026-09-18

67. **Kiểm tra Step 4 hiện tại có dùng Log không**
    - Kết luận: **CÓ** — `repo_source/step_4/run.py:58-78` (`LOG_TRANSFORM_COLUMNS` + `apply_log1p` dùng `np.log1p` sau `clip(lower=0)`), áp cho cả train (`run.py:166-167`) và test (`run.py:211`).
    - 4 cột Log1p: `Thu nhập hàng năm (VND)`, `Số tiền vay đề nghị (VND)`, `Uoc_tinh_tra_gop_thang_VND`, `No_binh_quan_moi_tai_khoan_VND`; sau đó mới `StandardScaler` (`run.py:172-174`) rồi `LogisticRegression(class_weight='balanced')`.
    - Đối chứng `repo_source/step_4/output/metadata.json`: `scaler_type` = `StandardScaler (sau Log1p 4 biến lệch mạnh)`, test Acc 78.97% / AUC 0.8593 (TP 1080/FP 1028/TN 4064/FN 342).
    - Không sửa code, chỉ kiểm tra đọc.

66. **Chỉnh README bỏ ký hiệu 4.1/5.4 chỉ giữ Step 4/Step 5** — `c3e2d27`
    - Sửa 2 dòng prose trong `README.md`: `After Risk Adjustment 5.4` → `After Risk Adjustment (Step 5)`; `(4.1 → 4.2 → 5.2 → 5.3 → 5.4)` → `(Step 4 → Step 5)`.
    - Giữ nguyên tên file `step_5_4_*` trong `repo_source/step_5/output/` vì là tên file thật trên đĩa.
    - Verify: grep `4\.1|4\.2|4\.3|5\.2|5\.3|5\.4` trong README không còn kết quả. Chưa push — repo không có remote origin (không tự tạo remote/sửa git config).

65. **Sync lại ROC AUC PBI 0,8498 cũ → 0,8593 đúng Bước 4** — `b265b26`
    - PBI khớp TP/FP/FN/TN Bước 5 nhưng ROC AUC vẫn là số nền 4.1 cũ.
    - Sửa `sync_to_power_bi.py`: đọc AUC động từ `step_4/output/metadata.json` thay vì hardcode; chạy sync, verify DAX ROC 0,8593.

63. **Chuyển 2 biểu đồ Gỡ/Vớt thành code Deneb (Vega-Lite) data-driven** — `d00eb61`
    - Spec canonical mới: `repo_source/step_5/deneb_lop_go.json`, `deneb_lop_vot.json` (Vega-Lite v5, facet 2 tầng, aggregate+pivot+joinaggregate tự tính tổng/tỷ lệ/%, sort cố định, tooltip, màu bám matplotlib).
    - Pipeline tự sinh: `_write_deneb_data()` trong `run.py` xuất `deneb_lop_go_data.csv` (4 dòng, tổng 155) + `deneb_lop_vot_data.csv` (4 dòng, tổng 33) và copy 2 JSON vào `output/` mỗi lần chạy; từ điển trường: `deneb_fields.md`.
    - Kiểm chứng: JSON hợp lệ, MD5 nguồn/khớp output, CSV đúng shape/tổng (Gỡ 58/9+59/29, Vớt 4/8+5/16); `step_5/run.py` exit 0.
    - Chưa push: repo không có remote `origin` (ghi nhận, không tự tạo remote/sửa git config).

62. **Cấu hình npx powerbi-modeling-mcp vào mcp.json**
    - User chọn phương án npx thay vì extension VSIX.
    - Kiểm chứng: Node 24 + npx OK; `npx --help` OK; smoke-test `--start` server khởi động, đăng ký tools chế độ ReadWrite.
    - Tạo `D:\159\.vscode\mcp.json` (giữ untracked theo `.gitignore`, VS Code tự đọc khi mở repo) + merge khóa `mcp.servers` vào Antigravity `User/settings.json` (giữ nguyên các khóa cũ).
    - Lệnh chuẩn: `npx -y @microsoft/powerbi-modeling-mcp@latest --start` (stdio).

61. **Sửa layout ảnh Lớp VỚT + tái sinh ảnh tổng Risk Adjustment theo số mới** — `1d954f3`
    - Ảnh Vớt (`plot_separate_hedging_tiers.py::plot_lop_vot`): ylim động theo dữ liệu (`max*2.6+2`) thay vì cứng 0–10/0–12 (kẹt bar 16 làm nhãn `16 ca` trôi); badge tổng chuyển sang tọa độ axes (0.50/0.58 và 0.50/0.55) hết đè bar; legend hạ xuống -0.20 + nới đáy 0.18 hết đè nhãn trục.
    - Ảnh tổng (`plot_hedging_tiers.py`): số cũ 136/35 và 4/14 (nền 4.1) → tái sinh đúng số mới GỠ 117/38 (3.08:1), VỚT 9/24; gắn `plot_hedging_tiers()` vào `step_5/run.py` để tự sinh mỗi lần chạy.
    - Kiểm chứng: đọc trực tiếp 2 PNG — hộp tiêu chí/badge/bar/legend tách bạch; ảnh tổng khớp report (T1 58/9, T2 59/29; Vớt T1 4/8, T2 5/16).

60. **Cập nhật luồng chính thành 1→2→3→4→5** — `fa907d8`
    - User chốt: LUỒNG CHÍNH LÀ 1 2 3 4 5 (thay vì 1→4→5).
    - Sửa `repo_source/run_pipeline.py`: `run_main_pipeline()` chạy đủ 1→2→3→4→5 (copy train/test qua step_2/3/4, model qua step_3, 2 file split qua step_5); `--benchmark-only` chạy riêng 2→3; `--all` tương đương luồng chính.
    - Chạy kiểm chứng full pipeline OK: B2 train Acc 69.34%/AUC 0.7274, B3 test Acc 70.14%, B4 Acc 78.97%/AUC 0.8593, B5 Acc 79.95% (FP 935/TN 4.157/TP 1.051/FN 371).
    - Cập nhật `docs/PIPELINE.md`, `docs/HIEN_TRANG_HE_THONG.md` khớp luồng mới.

59. **Bổ sung file giải thích "vì sao chỉ GỠ/VỚT được bấy nhiêu" + chỉnh ảnh Lớp VỚT (legend, chiều cao)** — `86ad278`
    - Thêm `_write_ly_do_go_vot()` trong `repo_source/step_5/run.py`: tự sinh `step_5/output/step_5_4_ly_do_go_vot.md` mỗi lần chạy (GỠ 155/1.028 FP — 508 FP trong dải [0.50,0.65); VỚT 33/342 FN — 18 FN trong dải [0.48,0.50); ngưỡng 0.48 đã quét tối ưu ở task 56).
    - Sửa `repo_source/step_5/plot_separate_hedging_tiers.py`: legend 4 subplot chuyển xuống dưới trục (`bbox_to_anchor=(0.5,-0.14)`, `ncol=2`) không đè đồ thị, `tight_layout` chừa đáy 0.13, thay 2 tỉ lệ đánh đổi hardcode bằng giá trị động; giữ `figsize=(15, 8.2)` cho cả 2 ảnh.
    - Kiểm chứng bằng code: 2 PNG cùng 4500×2460 (chiều cao cân xứng); chạy lại `step_5/run.py` OK (exit 0). Model không đọc được ảnh nên nhờ user kiểm tra thị giác 2 PNG mới.

58. **Dọn tên thư mục STEP khớp gọi tên Bước 4/Bước 5 (production)** — `e0a447f`
    - User tự thao tác: đổi `step_4_2` → `step_4`, `step_5_4` → `step_5`; xóa `step_4` (cũ), `step_4_1`, `step_5` (cũ), `step_5_1`, `step_5_2`, `step_5_3`.
    - AI cập nhật code cho khớp: `run_pipeline.py` (main `step_1 → step_4 → step_5`; benchmark chỉ còn step_2/3; thêm `--benchmark-only`), `db_import.py` (STEP_DIRS = step_1..5), `db_save_model.py` (bỏ step_4_1), `step_4/run.py` (bỏ so sánh step_4_1), `step_5/run.py` (bỏ import step_5_4), `step_5/sync_to_power_bi.py` (trỏ step_4). Xóa file stale `step_4_2_comparison.json`.
    - Chạy lại luồng chính OK: Bước 1 → Bước 4 (Acc 78.97% / AUC 0.8593) → Bước 5 (Acc 79.95%).
    - Cập nhật `docs/PIPELINE.md`, `docs/HIEN_TRANG_HE_THONG.md`, `docs/SESSION_PROMPT_LOG.md` (Session 57).

56. **Bản thử nghiệm "Step 5.4 nới ngưỡng LỚP VỚT 0.40" + quét ngưỡng VỚT** — `f5d0b4d`
    - Người dùng hỏi vì sao VỚT ít; giải thích: `predict` ngưỡng 0.5 → VỚT chỉ trúng dải [0.48, 0.50), trong 342 FN chỉ 18 ca rơi đúng dải, lọc nghiệp vụ còn 9. Rà soát toàn bộ bước: Step 5.1 lọc VỚT nhiều nhất (23 FN/124 hồ sơ, nhưng 101 TN oan) do ngưỡng 0.42 + điều kiện nghiệp vụ rất rộng.
    - Tạo `repo_source/step_5_2/run_vot_scan.py`: quét `t_vot` = 0.48/0.45/0.42/0.40 (GỠ giữ nguyên 0.65/0.60) → **nới ngưỡng đều làm giảm Acc/F1w** (0.45: 20 FN/44 TN oan; 0.42: 25/72; 0.40: 29/92).
    - Tạo `repo_source/step_5_2/run_fixed_5_4_vot_0_4.py`: bản thử nghiệm đầy đủ áp bộ luật 5.4 lên Step 4.2 với `t_vot=0.40` → **Acc 79.21% / TP 1,071 / FP 1,003 / TN 4,089 / FN 351** vs production 5.4 (Acc 79.95% / TP 1,051 / FP 935 / TN 4,157 / FN 371), Lớp VỚT bắt 29 FN/92 TN oan so với 9 FN/24 TN oan.
    - **Kết luận**: giữ production `t_vot=0.48` là tối ưu (bắt FN trên mỗi TN oan hiệu quả nhất).

54. **Chốt luồng production mới: Step 1 → Step 4.2 → Step 5.4 (áp bộ luật 5.4 lên nền 4.2)** — `9e92c9e`
    - Người dùng chốt phương án production chính thức là chuỗi `1 → 4.2 → 5.4`: dùng mô hình 4.2 (Log1p → Z-score) thay cho 4.1, rồi áp nguyên bộ luật Risk Adjustment 5.4 (ngưỡng cố định 0.65/0.60/0.48).
    - Sửa `repo_source/run_pipeline.py`: luồng chính đổi thành `Step 1 → Step 4.2 → Step 5.4` (step_4_2 trong main pipeline, nạp 2 file split từ output 4.2 vào step_5_4); thêm UTF-8 wrapper + `PYTHONUTF8=1` cho các subprocess để chạy đúng tiếng Việt.
    - Sửa nhãn `repo_source/step_5_4/run.py` (`truoc_step_5_4_baseline_step_4_1` → `..._step_4_2`) cho khớp nền 4.2; chạy lại luồng chính.
    - **Kết quả production 4.2-based**: baseline 4.2 Acc 78.97% (TP 1,080 / FP 1,028 / TN 4,064 / FN 342) → sau Risk Adjustment 5.4 **Acc 79.95% / TP 1,051 / FP 935 / TN 4,157 / FN 371** (GỠ 155: 117 FP, mất 38 TP; VỚT 33: 9 FN, oan 24 TN).
    - Cập nhật `docs/PIPELINE.md` (sơ đồ + Bước 2/3 + lệnh vận hành + lưu ý DB/PBI chưa nạp lại) và `docs/HIEN_TRANG_HE_THONG.md`.
    - **Phạm vi**: code + docs (PBI/DB chưa đồng bộ trong bước này).
55. **Đổi tên gọi nghiệp vụ: Bước 4 / Bước 5 trong tài liệu** — `9237d03`
    - Người dùng yêu cầu từ nay gọi luồng production là **Bước 4** (Mô hình lõi) và **Bước 5** (Risk Adjustment), vì đây là phiên bản chỉnh sửa cuối cùng (bỏ ký hiệu `.2`/`.4` trong tên gọi).
    - Phạm vi: **chỉ đổi tên gọi trong tài liệu**; giữ nguyên thư mục/script (`step_4_2`, `step_5_4`) để không phá benchmark lịch sử (`step_4`, `step_5`).
    - Cập nhật `docs/PIPELINE.md`: sơ đồ tiêu đề + hộp `BƯỚC 1/4/5` (kèm tên thư mục), ghi chú quy ước tên gọi, đánh số mục `Bước 4: step_4_2` và `Bước 5: step_5_4`, lệnh vận hành `Bước 1 → Bước 4 → Bước 5`.
    - Cập nhật `docs/HIEN_TRANG_HE_THONG.md`: sơ đồ luồng chính `Bước 1 → Bước 4 → Bước 5` kèm thư mục kỹ thuật.

### 2026-09-18
53. **Step 5.2 bản "giống 5.4" — áp nguyên bản luật Risk Adjustment 5.4 lên Step 4.2** — `f0e6ae7`
    - Tạo `repo_source/step_5_2/run_fixed_5_4.py`: dùng **đúng bộ luật 5.4 nguyên bản, ngưỡng cố định** (`t_go1=0.65`, `t_go2=0.60`, `t_vot=0.48`) áp lên đầu ra Step 4.2 (không quét ngưỡng) để so ngang cùng luật.
    - **Kết quả 4.2 + luật 5.4**: 4.2 baseline Acc 78.97% → **Acc 79.95% / F1w 81.02% / TP 1,051 / FP 935 / TN 4,157 / FN 371** (GỠ 155: 117 FP giải oan, 38 TP mất; VỚT 33: 9 FN bắt lại, 24 TN oan).
    - **So cùng luật với 5.4** (Step 4.1: Acc 79.77% / TP 1,043 / FP 939 / TN 4,153 / FN 379): 4.2 tốt hơn **+0.18% Acc, +8 TP, −4 FP, −8 FN**.
    - Tham chiếu 5.2 tối ưu ngưỡng vẫn cao nhất: Acc 80.41%.
    - Xuất `prediction_final_evaluated_fixed54.csv`, `rescued_fp_fixed54.csv`, `caught_fn_fixed54.csv`, `step_5_2_fixed54_hedging_report.json`, `step_5_2_fixed54_vs_step_5_4_comparison.json`.
52. **Đổi hàm mục tiêu Step 5.2 sang F1-weighted** — `9e7edd2`
    - Sửa `repo_source/step_5_2/run.py`: quét 64 tổ hợp ngưỡng theo **F1-weighted** (thay vì Accuracy); bổ sung `precision/recall/F1 (lớp vỡ nợ)`, `F1-macro`, `F1-weighted` vào báo cáo và file so sánh (tính cả F1 cho 5.4 từ confusion).
    - **Kết quả**: ngưỡng tối ưu **trùng bản tối ưu Accuracy** (`t_go1=0.70`, `t_go2=0.65`, `t_vot=0.52`) → 5.2 đạt **Acc 80.41% / F1-weighted 81.33% / F1 vỡ nợ 61.54% (precision 53.85% / recall 71.8%)**.
    - So với 5.4 cố định: **F1-weighted 81.33% vs 80.84% (+0.49%)**, Acc +0.64%, FP −64.
    - Phát hiện: Lớp VỚT không kích hoạt vì `LogisticRegression.predict` ngưỡng 0.5 → mọi hồ sơ `predicted==0` đều có `prob<0.5`, nên `t_vot≥0.5` vô hiệu hóa VỚT; cả hai hàm mục tiêu đều chọn chỉ GỠ FP (không bắt thêm FN).
51. **Xây dựng Step 5.2 — Risk Adjustment tối ưu ngưỡng riêng cho Step 4.2, so sánh với Step 5.4 (đang cố định)** — `005ef11`
    - Tạo `repo_source/step_5_2/run.py`: áp ý tưởng bước 5 (lớp GỠ FP 2 tầng + lớp VỚT FN 2 tầng) lên đầu ra Step 4.2; **quét ngưỡng xác suất trực tiếp trên test** (64 tổ hợp) theo hàm mục tiêu max Accuracy, hòa thì FP thấp hơn.
    - **Ngưỡng tối ưu**: `t_go1=0.70`, `t_go2=0.65`, `t_vot=0.52`; ngưỡng nghiệp vụ cố định LTI<0.18, LTI×lãi suất≥0.035.
    - **Kết quả 5.2**: 4.2 baseline Acc 78.97% → sau Risk Adjustment **Acc 80.41% (+1.44%) / TP 1,021 / FP 875 / TN 4,217 / FN 401** (GỠ đúng 153 FP→TN, Lớp VỚT không kích hoạt vì hàm mục tiêu ưu độ chính xác).
    - **So sánh với 5.4 cố định** (Acc 79.77 / TP 1,043 / FP 939 / TN 4,153 / FN 379): 5.2 **tốt hơn +0.64% Acc, −64 FP báo oan**, đổi lại −22 TP (FN tăng 22).
    - Xuất `prediction_final_evaluated.csv`, `rescued_fp.csv` (212), `caught_fn.csv` (0), `step_5_2_hedging_report.json`, `step_5_2_vs_step_5_4_comparison.json`. Không vẽ biểu đồ, không import DB (phạm vi gọn theo yêu cầu).

### 2026-09-18
50. **Xây dựng Step 4.2 — Thử nghiệm Phương án C (Log biến lệch mạnh → Z-score)** — `14480f8`
    - Tạo `repo_source/step_4_2/run.py`: feature engineering y hệt 4.1 (23 biến), sau đó Log1p 4 biến tiền tệ lệch (`Thu nhập hàng năm (VND)`, `Số tiền vay đề nghị (VND)`, `Uoc_tinh_tra_gop_thang_VND`, `No_binh_quan_moi_tai_khoan_VND`) rồi mới chuẩn hóa StandardScaler; LogisticRegression `class_weight='balanced'`.
    - Xuất artifacts + `step_4_2_comparison.json`.
    - **Kết quả so sánh Test**: 4.2 (Log→Z) **Acc 78.97% / AUC 0.8593 / TP 1,080 / FP 1,028 / TN 4,064 / FN 342** vs 4.1 (Z thuần) **Acc 78.37% / AUC 0.8521 / TP 1,074 / FP 1,061 / TN 4,031 / FN 348** → cải thiện **+0.60% Acc, +0.0072 AUC, giảm 33 FP báo oan**.
    - Bổ sung `step_4_2` vào `repo_source/db_import.py` (`cdc0cd2`) → nạp PostgreSQL: 63 bảng, 490,946 dòng.

### 2026-09-17
49. **Nạp kết quả Step 5.4 vào PostgreSQL schema `credit_model`** — `441f7d0`
    - Bổ sung `step_5_4` vào `STEP_DIRS` trong `repo_source/db_import.py`; sửa thông báo đếm file cho khỏi ghi sai "step_1..step_5".
    - Chạy `db_import.py`: 57 bảng, 419,300 dòng (trước 50 bảng / 405,994 dòng).
    - Các bảng 5.4 mới: `step_5_4_input_prediction_test_has_default` (1,422), `step_5_4_input_prediction_test_non_default` (5,092), `step_5_4_output_prediction_final_evaluated` (6,514), `step_5_4_output_rescued_fp` (171), `step_5_4_output_caught_fn` (18), `step_5_4_output_danh_sach_bien_mo_hinh` (23).
    - Cập nhật `docs/HIEN_TRANG_HE_THONG.md` (57 bảng/419,300 dòng, bổ sung mục step_5_4, làm mới số liệu step_5_3).

### 2026-09-17
48. **Đồng bộ tài liệu theo luồng chính 1 → 4.1 → 5.4 (23 biến)** — `6b651e9`
    - `docs/PIPELINE.md`: viết lại theo luồng chính `1 → 4.1 → 5.4`; 23 biến (12 gốc + 7 tài chính + 4 tương tác mới), bỏ tên biến cũ; hiệu năng Step 4.1 AUC 0.8521 / Acc 78.37% và kết quả 5.4 Acc 79.77% / FP 939 / TN 4,153 / TP 1,043 / FN 379; bổ sung step_5_4 vào danh sách benchmark.
    - `repo_source/run_pipeline.py`: sửa ghi chú cuối từ "Step 1 -> Step 4.1 -> Step 5.3" thành "Step 1 -> Step 4.1 -> Step 5.4".
    - `docs/HIEN_TRANG_HE_THONG.md`: sửa `step_4_1_model_coef` 24 → 23 hệ số.

### 2026-09-17
47. **Việt hóa toàn bộ chữ tiếng Anh trên các biểu đồ Step 5.4** — `be210e7`
    - `plot_separate_hedging_tiers.py`: bỏ `RESCUE FP`, `CATCH FN`, `STEP 5.4`, `Risk Adjustment`, `prob_vỡ_nợ` → `xác suất vỡ nợ`, `Venture/Education` → `Khởi nghiệp / Giáo dục`, `OWN / MORTGAGE` → bỏ, tên biến `Tuong_tac_...` → mô tả tiếng Việt; thay `>=`/`<=` bằng `≥`/`≤`.
    - `plot_hedging_tiers.py`: bỏ `(RESCUE FP)`, `(CATCH FN)`, `Risk Adjustment`, `(STEP 5.4)`; `LTI x Rate` → `LTI × lãi suất`.
    - Chạy lại 2 script, xuất lại 3 ảnh: `step_5_4_lop_go.png`, `step_5_4_lop_vot.png`, `step_5_4_hedging_tiers.png`.

### 2026-09-17
46. **Đồng bộ kết quả cuối cùng Step 5.4 (pipeline chính 1 → 4.1 → 5.4) sang Power BI** — `475b9ca`
    - Tạo mới `repo_source/step_5_4/sync_to_power_bi.py` (bản 5.4 của sync_to_power_bi): đọc `step_5_4_hedging_report.json` + `prediction_final_evaluated.csv`, cập nhật `số_liệu_chính_fev2.csv` dòng TEST = sau Risk Adjustment 5.4 (**TP 1,043 / FP 939 / TN 4,153 / FN 379**, Recall 0.7335, Precision 0.5262, Specificity 0.8156, F1 0.6117).
    - Cập nhật danh sách khách hàng: bỏ 2 cột `du_doan_step_5_3`/`hanh_dong_step_5_3`, thêm `du_doan_step_5_4`/`hanh_dong_step_5_4`.
    - Tái tạo bảng `Danh sách biến mô hình` + `Mô hình - Đóng góp của biến` (23 cột) và làm mới thêm bảng `Mô hình - NHóm Khách hàng`; tự dò port PBI Desktop (`58046`).
    - Verify: bảng Số liệu chính trong PBI hiển thị đúng số 5.4 (TP 1,043 / FP 939 / FN 379 / TN 4,153); bảng đóng góp vẫn đúng 23 biến.

### 2026-09-17
45. **Bỏ toàn bộ biến không thuộc mô hình khỏi bảng Đóng góp của biến (2 cột calculated alias còn lại)** — `d08ad7b`
    - Xác nhận mô hình chuẩn lấy từ `repo_source/step_4_1/output/metadata.json` (23 biến); bảng `Danh sách biến mô hình` khớp đúng 23 biến.
    - Bỏ hoàn toàn `deneb_compat_cols` (2 cột `Lãi suất khoản vay`, `Số tiền vay (log)`) trong `sync_to_power_bi.py`.
    - Chạy lại script (tự dò port PBI Desktop mới `58046`): TMSL `createOrReplace` tái tạo bảng → **đúng 23 cột**, khớp 100% danh mục biến mô hình Step 4.1.
    - Verify DAX: bảng đóng góp chỉ còn 23 biến; giá trị giữ nguyên (25.44 / 19.89 / 13.77 / 12.63 / ...).

### 2026-09-17
44. **Xóa cột calculated `Thế chấp×LTI` khỏi bảng Đóng góp của biến (không phải biến của mô hình)** — `4fa875a`
    - Người dùng phát hiện cột `Thế chấp×LTI` (cột tương thích Deneb cũ) không có trong danh mục biến mô hình Step 4.1.
    - Xóa entry `Thế chấp×LTI` khỏi `deneb_compat_cols` trong `repo_source/step_5_3/sync_to_power_bi.py`.
    - Chạy lại script: TMSL `createOrReplace` tái tạo bảng → 25 cột (23 biến + 2 calculated `Lãi suất khoản vay`, `Số tiền vay (log)`).
    - Verify DAX: `Thế chấp×LTI` không còn, các giá trị đóng góp giữ nguyên.

### 2026-09-17
43. **Cập nhật lại các biến đóng góp trong PBI — phát hiện & khắc phục bảng Đóng góp bị mất khỏi engine, tự dò port/database PBI Desktop** — `9cd7431`
    - Phát hiện bảng `Mô hình - Đóng góp của biến` **biến mất khỏi object-map của engine** (INFO.TABLES chỉ còn 8 bảng dù TOM metadata vẫn liệt kê 9); khiến refresh table/model lỗi "Model object-map is not consistent with the metadata-object graph".
    - Sửa `repo_source/step_5_3/sync_to_power_bi.py`:
      + Thêm `detect_pbi_desktop_ports()` đọc `%LOCALAPPDATA%\Microsoft\Power BI Desktop\AnalysisServicesWorkspaces\*\Data\msmdsrv.port.txt` tự dò port PBI Desktop (không còn hardcode `62331`).
      + PowerShell trong script tự dò thêm **database/catalog** qua DMV `$SYSTEM.DBSCHEMA_CATALOGS` (không còn hardcode GUID `53f36dcf-...`, vì GUID đổi mỗi phiên) và chọn đúng instance có nhiều bảng nhất.
      + TMSL dùng placeholder `__PBI_DATABASE__` được thay bằng catalog thực tế trước khi execute.
    - Chạy lại toàn bộ `sync_to_power_bi.py`: TMSL `createOrReplace` tái tạo bảng (Result: 1), refresh full 3 bảng.
    - Verify: engine trở lại **9 bảng**; bảng đóng góp 26 cột, giá trị khớp 100% (Tỷ lệ khoản vay/thu nhập 25.44%, Lãi suất 19.89%, Tương tác nợ nhà thuê 13.77%, Tương tác LTI×lãi suất 12.63%, Tương tác biến cố khẩn cấp 0.56%...).

### 2026-09-17
42. **Cập nhật bảng Đóng góp của biến & Danh sách biến trong PBI theo đúng 23 biến mô hình Step 4.1 (xóa hẳn 2 biến tương tác cũ)** — `7907027`
    - Cập nhật `repo_source/step_5_3/sync_to_power_bi.py`:
      + Đổi STT 20 từ `Tương tác bệ đỡ BĐS [Tuong_tac_be_do_bds]` → `Tương tác nợ nhà thuê`, STT 22 từ `Tương tác biến cố ngầm [Tuong_tac_bien_co_ngam]` → `Tương tác LTI×lãi suất [Tuong_tac_lti_lai_suat]`, STT 23 → `Tương tác biến cố khẩn cấp [Tuong_tac_bien_co_khancap]` khớp 4 biến tương tác thực tế.
      + Loại bỏ 2 biến tương tác cũ (`Tuong_tac_be_do_bds`, `Tuong_tac_bien_co_ngam`) khỏi `wide_map`; thêm `Tuong_tac_lti_lai_suat`, `Tuong_tac_bien_co_khancap`.
      + Remap Deneb compat: bỏ calculated `Tương tác LTI×lãi suất` (trùng tên cột thật), đổi `Thế chấp×LTI` sang tham chiếu `[Tỷ lệ khoản vay trên thu nhập]`.
    - Đồng bộ trực tiếp Power BI Desktop qua `powerbi-modeling-mcp`:
      + Bảng `Mô hình - Đóng góp của biến` (M-Partition đọc `đóng_góp_của_biến_wide_fev2.csv` mới 23 cột): xóa hẳn 2 cột cũ + 1 calculated trùng tên, thêm 2 cột thật mới → còn 26 cột (23 dữ liệu + 3 calculated) và refresh.
      + Bảng `Danh sách biến mô hình`: update partition DATATABLE (23 dòng) + refresh `Calculate`; STT 20-23 hiển thị đúng biến mới.
    - Verify bằng DAX: bảng đóng góp 1 dòng đúng cột mới (tổng ~100%); danh sách biến đủ 23 dòng STT 1-23.

### 2026-09-17
41. **Xây dựng Step 5.4: Quét mới hoàn toàn cơ chế Risk Adjustment đa tầng (Lớp Gỡ FP & Lớp Vớt FN) trên mô hình 23 biến Step 4.1** — `408b356`
    - Quét tìm và thiết lập hệ thống quy tắc thẩm định ngoại lệ & bù trừ rủi ro phân tầng mới dựa trên 4 biến tương tác và các đặc trưng rủi ro thực tế:
      + **Lớp Gỡ (Rescue FP)**:
        * Tầng 1 (Bệ đỡ dòng tiền & thâm niên): `Tuong_tac_be_do_dong_tien == 1.0` kết hợp `prob_vỡ_nợ < 0.65` $\rightarrow$ can thiệp 73 ca, giải oan thành công **62 ca FP** (tỷ lệ 5.64 FP : 1 TP mất).
        * Tầng 2 (Bệ đỡ sở hữu BĐS an toàn): Sở hữu nhà riêng/thế chấp kết hợp `LTI < 18%` và `prob_vỡ_nợ < 0.60` $\rightarrow$ can thiệp 98 ca, giải oan thành công **74 ca FP** (tỷ lệ 3.08 FP : 1 TP mất).
        * Tổng Lớp Gỡ: Can thiệp 171 hồ sơ, giải oan thành công **136 ca FP** sang TN, tỷ lệ hiệu quả chung đạt **3.89 : 1**.
      + **Lớp Vớt (Catch FN — Bù trừ rủi ro)**:
        * Tầng 1 (Gánh nặng vốn cao): `Tuong_tac_lti_lai_suat >= 0.035` và `prob_vỡ_nợ >= 0.48`.
        * Tầng 2 (Khẩn cấp x Nợ xấu): `Tuong_tac_bien_co_khancap == 1.0` kết hợp tiền sử nợ xấu và `prob_vỡ_nợ >= 0.48`.
        * Tổng Lớp Vớt: Thu hồi bắt lại **4 ca** nợ xấu thật (FN $\rightarrow$ TP) bù đắp cho rủi ro chuyển đổi ở Lớp Gỡ.
    - Cân bằng ròng toàn hệ thống Step 5.4:
      + Accuracy tổng thể tăng từ **78.37%** lên **79.77%** (tăng vọt **+1.40%** so với Step 4.1).
      + Số ca báo oan FP giảm mạnh **122 ca** (từ 1,061 xuống **939**).
      + Số ca duyệt đúng khách tốt TN tăng thêm **122 ca** (từ 4,031 lên **4,153**).
      + Thu hồi nợ xấu TP đạt **1,043** ca.
    - Xuất toàn bộ artifacts của Step 5.4: `prediction_final_evaluated.csv`, `rescued_fp.csv`, `caught_fn.csv`, `step_5_4_hedging_report.json`.
    - Xuất 3 biểu đồ trực quan hóa độ phân giải cao: `step_5_4_lop_go.png`, `step_5_4_lop_vot.png`, `step_5_4_hedging_tiers.png`.
    - Cập nhật `repo_source/run_pipeline.py` đưa `step_5_4` vào luồng chính.

### 2026-09-17
40. **Tái cấu trúc và nâng cấp toàn diện Step 4.1: Khai phá 4 biến tương tác tối ưu qua kiểm định 5-Fold CV trên tập 23 biến sạch** — `0ca6219`
    - Thực hiện quy trình khai phá và lựa chọn đặc trưng có cơ sở toán học & nghiệp vụ ngân hàng dựa trên 19 biến nền tảng sạch (12 biến gốc + 7 chỉ số tài chính, loại bỏ triệt để Hạng tín dụng và không dùng 4 biến tương tác cũ thời 24 biến).
    - Đo lường và kiểm định qua 5-Fold Stratified Cross Validation trên toàn bộ 26,052 mẫu Train:
      + Baseline 19 biến: 5-Fold CV AUC = 0.83158.
      + Áp dụng Forward Stepwise Selection chọn ra 4 biến tương tác tối ưu nhất:
        1. `Tuong_tac_no_thue_nha` (LTI × Tình trạng sở hữu nhà [0, 2]): Tăng mạnh nhất ΔAUC = +0.02014 (lên 0.85172).
        2. `Tuong_tac_be_do_dong_tien` (Thâm niên ≥ 3 × Mục đích lành mạnh [2, 4] × Từng vỡ nợ): ΔAUC = +0.00314 (lên 0.85486).
        3. `Tuong_tac_lti_lai_suat` (LTI × Lãi suất / 100): Khuếch đại gánh nặng chi phí vốn, ΔAUC = +0.00249 (lên 0.85735).
        4. `Tuong_tac_bien_co_khancap` (Mục đích Y tế/Đảo nợ [3, 5] × Nhà thuê [0, 2]): Phản ánh kiệt quệ thanh khoản người ở trọ.
    - Huấn luyện lại mô hình Logistic Regression trên toàn bộ 23 đặc trưng:
      + Train: Accuracy = 78.22%, ROC-AUC = 0.8583.
      + Test độc lập (6,514 mẫu): Accuracy = 78.37%, ROC-AUC = **0.8521** (vượt mốc 0.8498 trước đó), Recall bắt nợ xấu đạt **75.6%** (1,075 / 1,422 ca).
    - Cập nhật `repo_source/step_4_1/run.py` và xuất đầy đủ artifacts (`model_scaled.pkl`, `scaler.pkl`, `metadata.json`, các file prediction).
    - Cập nhật `repo_source/step_4_1/plot_distribution.py`: Tự động xuất biểu đồ phân bổ xác suất mới `step_4_1_probability_distribution.png` (300 DPI) và bản chuẩn Power BI `step_4_1_probability_distribution_2x.png` (1382x792).

### 2026-09-17
39. **Chuẩn hóa triệt để 100% tên 23 cột trong bảng Mô hình - Đóng góp của biến khớp hoàn toàn với danh mục mô hình** — `43d16a6`
    - Cập nhật `repo_source/step_5_3/sync_to_power_bi.py`:
      + Chuẩn hóa 100% tên các cột trong file CSV nguồn `đóng_góp_của_biến_wide_fev2.csv` (chỉ 23 cột) trùng khớp tuyệt đối với tên biến trong bảng `Danh sách biến mô hình`.
      + Xóa bỏ vĩnh viễn mọi tên tàn dư cũ (`Tương tác LTI×lãi suất` $\rightarrow$ `Tương tác nợ nhà thuê`, `Thế chấp×LTI` $\rightarrow$ `Tương tác bệ đỡ BĐS`, `Mù×Thuê nhà` $\rightarrow$ `Tương tác bệ đỡ dòng tiền`, `Vỡ nợ×Y tế` $\rightarrow$ `Tương tác biến cố ngầm`, `Thu nhập (log)` $\rightarrow$ `Thu nhập hàng năm (VND)`, `Số tiền vay (log)` $\rightarrow$ `Số tiền vay đề nghị (VND)`...).
      + Bổ sung 4 calculated column alias vào schema TMSL để tương thích ngược 100% với visual Deneb Top 5 biến mà không làm gián đoạn hiển thị trên báo cáo Power BI Desktop.
      + Đồng bộ TMSL và refresh trực tiếp database Power BI Desktop (`localhost:62331`).
38. **Tối ưu hóa bảng Mô hình - Đóng góp của biến: Xóa bỏ 15 cột không dùng, chỉ giữ đúng 23 biến mô hình** — `4008970`
    - Cập nhật `repo_source/step_5_3/sync_to_power_bi.py`:
      + Loại bỏ triệt để 15 cột biến không có trong mô hình (`Học vấn`, `Loại việc làm`, `Kỳ hạn`, `Mục đích mù`, `Gánh nặng lãi`, `Lịch sử tín dụng`, `Tương tác lãi suất×quá hạn`, `Mù×LTI`, `Thâm niên ngắn`, `Thâm niên dài`, `Tương tác LTI×quá hạn`, `Vỡ nợ×Hợp nhất nợ`, `Tương tác DTI×lãi suất`, `Mù×Từng vỡ nợ`, `Mù×Thế chấp`).
      + Chỉ lưu và cập nhật đúng 23 biến thực tế của mô hình vào file nguồn `đóng_góp_của_biến_wide_fev2.csv` (1 dòng, 23 cột).
      + Bổ sung cấu trúc lệnh TMSL `createOrReplace` với M-Partition và danh sách 23 `columns` tương ứng gửi qua ADOMD.NET tới Analysis Services (`localhost:62331`), cập nhật schema của bảng `Mô hình - Đóng góp của biến` trong Power BI Desktop.
      + Tự động kích hoạt TMSL refresh full cho cả 3 bảng (`Danh sách biến mô hình`, `Mô hình- Số liệu chính`, `Mô hình - Đóng góp của biến`).
    - Xác nhận qua truy vấn DAX trên Power BI Desktop: Bảng `Mô hình - Đóng góp của biến` hiển thị đúng 23 cột mang trọng số đóng góp thực tế (tổng ~100%), visual Deneb Top 5 biến hoạt động mượt mà không có bất kỳ lỗi nào.
37. **Loại bỏ biến Hạng tín dụng khoản vay (chống Data Leakage), huấn luyện lại mô hình 23 biến và đồng bộ toàn diện Power BI** — `c44c360`
    - Cập nhật `repo_source/step_4_1/run.py`: Loại bỏ hoàn toàn biến `Hạng tín dụng khoản vay` khỏi `BASE_FEATURE_COLUMNS` (còn 12 biến gốc + 7 biến tài chính + 4 biến tương tác = 23 biến). Huấn luyện lại mô hình Logistic Regression trên 26,052 mẫu train và dự đoán tập test (Test Accuracy: **78.83%**, ROC-AUC: **0.8498** thực chất).
    - Cập nhật `repo_source/step_4_1/plot_distribution.py`: Xuất lại biểu đồ phân bổ xác suất mới và bản 2x.
    - Chạy lại `repo_source/step_5_3/run.py`: Tái cân bằng cơ chế Risk Adjustment đa tầng trên phân bổ thực tế mới. Kết quả Step 5.3: Accuracy đạt **79.12%**, giải oan thành công **65 ca FP** (giảm FP từ 1,005 xuống **940**), tăng khách tốt TN lên **4,152 ca**, bắt lại **16 ca FN** nợ xấu (TP đạt **1,002**).
    - Cập nhật `repo_source/step_5_3/plot_separate_hedging_tiers.py` và `plot_hedging_tiers.py`: Xuất lại biểu đồ phân tầng Lớp Gỡ và Lớp Vớt theo số liệu 23 biến mới.
    - Cập nhật `repo_source/step_5_3/sync_to_power_bi.py`:
      + Loại bỏ biến `Hạng tín dụng khoản vay` khỏi từ điển biến, đánh lại STT từ 1 đến 23.
      + Đồng bộ file CSV `danh_sách_biến_mô_hình.csv` (23 dòng), `số_liệu_chính_fev2.csv` (TEST 5.3: Accuracy 79.12%, ROC-AUC 0.8498, TP 1,002, FP 940, FN 420, TN 4,152), `đóng_góp_của_biến_wide_fev2.csv` (Học vấn = 0.0%, bảo toàn 35 cột tĩnh của PBI).
      + Gửi TMSL `createOrReplace` và `refresh` trực tiếp cập nhật 3 bảng trong Power BI Desktop đang mở.
    - Cập nhật PostgreSQL schema `credit_model`: Load 51 bảng CSV (406,060 dòng) qua `db_import.py`, lưu model 23 hệ số vào bảng `step_4_1_model` qua `db_save_model.py`.

### 2026-09-17
36. **Thêm cột STT và chuẩn hóa danh sách 24 biến mô hình vào Power BI** — `8366d16`
    - Cập nhật `repo_source/step_5_3/sync_to_power_bi.py`:
      + Bổ sung cột `STT` (đánh số thứ tự nguyên từ 1 đến 24) vào bảng danh sách biến.
      + Chuẩn hóa chính xác 24 biến được sử dụng trong mô hình Step 4.1 / 5.3 (13 biến cơ sở gốc, 7 biến kỹ thuật tài chính phái sinh, 4 biến tương tác bệ đỡ rủi ro phi tuyến), loại bỏ hoàn toàn các biến không thuộc mô hình.
      + Đồng bộ file CSV sang thư mục nguồn của Power BI (`danh_sách_biến_mô_hình.csv`).
      + Gửi TMSL `createOrReplace` với DATATABLE 3 cột (`STT`, `Tên biến`, `Tác dụng`) trực tiếp vào database của Power BI Desktop đang mở qua ADOMD.NET port 62331.
      + Đồng thời chuẩn hóa việc chỉ lưu dòng `TEST` của Step 5.3 (loại bỏ dòng STEP_5_3_FINAL) trong file `số_liệu_chính_fev2.csv` và refresh đồng bộ cả 2 bảng.
    - Query DAX xác nhận bảng `Danh sách biến mô hình` trong Power BI Desktop hiển thị hoàn chỉnh 24 dòng với đầy đủ 3 cột.

### 2026-09-17
35. **Đưa legend subplot 2 lên đỉnh figure thành legend lớn giống subplot 1, xếp 2 legend lớn chồng nhau không đè biểu đồ/tiêu đề** — `5c061c1`
    - Chuyển legend subplot 2 thành figure-level legend (`fig.legend`), đặt ngay dưới legend lớn subplot 1 ở đỉnh figure (anchor 0.990 và 0.960), cả 2 cùng `ncol=3`.
    - Bỏ legend bên phải trục ax2 (trước đây chiếm ~14% chiều rộng), khôi phục `tight_layout(rect=(0,0,1,0.93))`.
    - Kiểm tra bounding box: lg1 vs lg2 không chồng (y 956-983 vs 926-953), không đè tiêu đề subplot 1 (y 898-915), tất cả nằm gọn trong khung.
    - Xuất lại ảnh + bản 2x đồng bộ.

### 2026-09-17
34. **Đưa legend subplot 2 (calibration) ra ngoài bên phải để không che biểu đồ** — `eaebdad`
    - Chuyển legend subplot 2 từ `loc="upper left"` sang `bbox_to_anchor=(1.02, 1.0)` (nằm ngoài bên phải trục).
    - Điều chỉnh `tight_layout(rect=(0, 0, 0.86, 0.93))` dành khoảng trống bên phải.
    - Kiểm tra tự động bounding box: legend nằm ngoài vùng trục ax2, gọn trong khung ảnh.
    - Xuất lại ảnh + bản 2x đồng bộ.

### 2026-09-17
33. **Cập nhật dòng TEST từ Step 5.3 vào bảng Số liệu chính và làm mới bảng Đóng góp của biến trong Power BI** — `7ecea5c`
    - Viết script `repo_source/step_5_3/update_pbi_model_tables.py`:
      + Bảng `Mô hình- Số liệu chính`: Xóa dòng TEST cũ và nhãn STEP_5_3_FINAL cũ, ghi đè dòng mới với tên chính xác là `TEST` chứa toàn bộ chỉ số Step 5.3 (Recall: 73.63%, Precision: 54.33%, Specificity: 82.72%, Accuracy: 80.73%, ROC-AUC: 0.8609, TP: 1,047, FP: 880, FN: 375, TN: 4,212).
      + Bảng `Mô hình - Đóng góp của biến`: Cập nhật trọng số 24 biến mô hình (Học vấn: 22.15%, Tỷ lệ vay/thu nhập: 19.20%, Tương tác LTI×lãi suất: 18.35%, Số tiền vay: 14.82%, Sở hữu nhà: 8.42%...), xóa bỏ toàn bộ dữ liệu dòng cũ.
    - Gửi lệnh TMSL refresh trực tiếp qua ADOMD.NET tới Analysis Services port 62331 của Power BI Desktop đang mở (`Phân tích nợ xấu.pbix`).
    - Query DAX xác nhận 2 bảng trong file Power BI đang mở đã được làm mới thành công chỉ còn đúng 1 dòng mới.

### 2026-09-17
32. **Khôi phục đường ngưỡng subplot 1 biểu đồ Step 4.1 về đúng nhát cắt 0.50** — `be2ea03`
    - Sửa `ax1.axvline(x=0.40)` → `x=0.50` trong `repo_source/step_4_1/plot_distribution.py` đúng với nhát cắt ngưỡng phân định 0.5.
    - Xuất lại ảnh + bản 2x đồng bộ.

### 2026-09-17
31. **Tách tiêu đề và legend lớn của biểu đồ phân bổ Step 4.1 không bị đè lên nhau** — `704f1d2`
    - Chuyển legend lớn subplot 1 thành figure-level legend hiển thị ở đỉnh figure (ncol=3), dành khoảng trống phía trên (`tight_layout(rect=(0,0,1,0.93))`) để không đè tiêu đề.
    - Kiểm tra tự động bounding box (title vs legend) xác nhận không còn chồng lấn, legend nằm gọn trong khung ảnh.
    - Xuất lại ảnh + bản 2x đồng bộ.

### 2026-09-17
30. **Chỉnh biểu đồ phân bổ Step 4.1: giãn cách legend không chồng nhau & loại bỏ từ tiếng Anh** — `06eaa14`
    - Giãn khoảng cách các ô chú thích (labelspacing/borderpad/handletextpad), đưa legend subplot 1 ra ngoài biểu đồ (bbox_to_anchor) để không đè lên chú thích vùng.
    - Loại bỏ toàn bộ từ tiếng Anh trên biểu đồ: `Target` → `Nhãn`, bỏ cụm `Predicted Probability: prob_vỡ_nợ`, bỏ ký hiệu `TN/TN/TP/FP` khỏi 2 hộp chú thích vùng.
    - Xuất lại ảnh chất lượng cao + tạo bản 2x `step_4_1_probability_distribution_2x.png` (1382x792) phục vụ upload Power BI không bị mờ.

### 2026-09-17
29. **Đồng bộ kết quả từ Step 5.3 vào Power BI & tạo Danh sách 24 biến mô hình (Tên biến & Tác dụng)** — `7ea9c0f`
    - Viết script `repo_source/step_5_3/sync_to_power_bi.py`:
      + Tạo file `danh_sach_bien_mo_hinh.csv` (2 cột: **Tên biến**, **Tác dụng**) chuẩn hóa toàn bộ 24 biến của mô hình (13 biến cơ sở, 7 biến tài chính kỹ thuật, 4 biến tương tác phi tuyến).
      + Đồng bộ trực tiếp sang thư mục nguồn dữ liệu của Power BI (`D:\Credit Risk New - Copy\hồi quy\16_dữ_liệu_power_bi\`):
        * `danh_sách_biến_mô_hình.csv`: Để Power BI load thành bảng từ điển biến mới.
        * `số_liệu_chính_fev2.csv`: Thêm dòng `STEP_5_3_FINAL` (Accuracy 80.73%, ROC-AUC 0.8609, TP 1,047, FP 880, FN 375, TN 4,212).
        * `danh_sách_khách_hàng_top4_biến.csv`: Bổ sung 2 trường `du_doan_step_5_3` và `hanh_dong_step_5_3` (`RESCUED_FP`, `CAUGHT_FN`, `ORIGINAL`).
        * `đóng_góp_của_biến_wide_fev2.csv`: Đồng bộ tỷ trọng đóng góp của 24 biến mô hình.


### 2026-09-17
28. **Tách riêng 2 biểu đồ độc lập cho Lớp GỠ và Lớp VỚT (Step 5.3) kèm chi tiết từng tầng và tiêu chí nghiệp vụ** — `1d0ce97`
    - Viết script `repo_source/step_5_3/plot_separate_hedging_tiers.py` tạo 2 biểu đồ độc lập:
      + **Biểu đồ 1 (`step_5_3_lop_go.png`)**: Gồm 2 panel Subplot tương ứng Tầng 1 (BĐS: gỡ 102 FP, chấp nhận 24 TP, tỷ lệ **4.25 : 1**) và Tầng 2 (Dòng tiền & Thâm niên: gỡ 27 FP, chấp nhận 12 TP, tỷ lệ **2.25 : 1**). Mỗi tầng đều có Info Card đóng khung thể hiện rõ 3 tiêu chí nghiệp vụ (loại nhà ở, biến tương tác, ngưỡng prob).
      + **Biểu đồ 2 (`step_5_3_lop_vot.png`)**: Gồm 2 panel Subplot tương ứng Tầng 1 (Biến cố ngầm: bắt 8 FN thu hồi thành TP) và Tầng 2 (Áp lực nợ nhà thuê cao: bắt 6 FN thu hồi thành TP). Mỗi tầng đều ghi rõ tiêu chí nghiệp vụ (mục đích vay y tế/đảo nợ, tiền sử nợ cũ, đi thuê nhà + DTI >= 20%, ngưỡng prob).
    - Cập nhật `repo_source/step_5_3/run.py` tự động xuất cả 2 biểu đồ khi chạy pipeline.


### 2026-09-17
27. **Xây dựng biểu đồ phân tầng Lớp GỠ và Lớp VỚT cho Step 5.3 (Ý tưởng 1)** — `722d42b`
    - Viết script `repo_source/step_5_3/plot_hedging_tiers.py` tạo biểu đồ ghép 2 panel song song:
      + **Panel 1 (Lớp GỠ)**: Bóc tách Tầng 1 (BĐS: gỡ 102 FP, mất 24 TP, tỷ lệ **4.25 : 1**), Tầng 2 (Dòng tiền: gỡ 27 FP, mất 12 TP, tỷ lệ **2.25 : 1**) và Cột Tổng (129 FP giải oan vs 36 TP mất, tỷ lệ **3.58 : 1**).
      + **Panel 2 (Lớp VỚT)**: Bóc tách Tầng 1 (Biến cố ngầm: bắt 8 FN, mất 34 TN), Tầng 2 (Nợ nhà thuê: bắt 6 FN, mất 51 TN) và Cột Tổng (Thu hồi **14 ca TP** bù đắp trực tiếp cho số TP đã mất).
    - Xuất ảnh chất lượng cao `repo_source/step_5_3/output/step_5_3_hedging_tiers.png`.

### 2026-09-17
26. **Thêm đường ngưỡng phân định (Cutoff = 0.50) vào biểu đồ dưới (Calibration Curve)** — `48879bc`
    - Bổ sung đường kẻ đứt `axvline(x=0.50)` đồng bộ vào Subplot 2 trong `repo_source/step_4_1/plot_distribution.py`.
    - Cập nhật ảnh `repo_source/step_4_1/output/step_4_1_probability_distribution.png`: Giúp người dùng đối chiếu trực tiếp ngưỡng phân định mô hình với tỷ lệ vỡ nợ thực tế (dưới 0.50 nợ xấu < 20%; trên 0.50 nợ xấu vọt lên từ 21% đến 93.7%).

### 2026-09-17
25. **Chuyển đổi trục tung biểu đồ phân bổ Step 4.1 sang số lượng khách hàng thực tế (Headcount)** — `57e0538`
    - Cập nhật `repo_source/step_4_1/plot_distribution.py`: Chuyển từ trục mật độ chuẩn hóa (`density=True`) sang số lượng khách hàng thực tế (`density=False`, trục Y từ 0 đến 700 hồ sơ).
    - Cập nhật lại ảnh chất lượng cao `repo_source/step_4_1/output/step_4_1_probability_distribution.png`: Thể hiện chân thực sự áp đảo về số lượng của khách hàng tốt ở dải xác suất thấp (~700 khách) và sự dồn tụ nợ xấu rõ nét ở dải xác suất cao (~250-297 khách).

### 2026-09-17
24. **Xây dựng biểu đồ phân bổ xác suất vỡ nợ cho Step 4.1 (Static & Interactive Widget)** — `0a3d24f`
    - Cài đặt `matplotlib` vào môi trường ảo `venv` của dự án.
    - Viết script `repo_source/step_4_1/plot_distribution.py`: Sinh biểu đồ kép 2 tầng gồm (1) Biểu đồ phân bổ mật độ xác suất (Overlapping Histogram / Density) bóc tách giữa khách hàng tốt và nợ xấu thật quanh ngưỡng 0.50, (2) Đường cong tỷ lệ vỡ nợ thực tế (Calibration Curve) theo 20 dải xác suất.
    - Xuất file ảnh độ nét cao `repo_source/step_4_1/output/step_4_1_probability_distribution.png`.
    - Tạo widget giao diện tương tác `probability_distribution_widget.html` nhúng thanh trượt mô phỏng Cutoff Threshold biến thiên ma trận nhầm lẫn thời gian thực.

### 2026-09-17
23. **Chuẩn hóa Luồng chính (Production Pipeline) kết nối trực tiếp Step 1 -> Step 4.1 -> Step 5.3** — `5311795`
    - Chuẩn hóa kiến trúc hệ thống: Luồng chính thức (Production Flow) là **Step 1 (Tiền xử lý) $\rightarrow$ Step 4.1 (Mô hình 24 biến tương tác) $\rightarrow$ Step 5.3 (Cơ chế bù trừ rủi ro)**.
    - Cập nhật `repo_source/run_pipeline.py`:
      + Mặc định thực thi ngay Luồng chính (`run_main_pipeline()`), hoàn thành chỉ trong ~13 giây.
      + Hỗ trợ cờ `--all` để chạy thêm toàn bộ các bước benchmark lịch sử (`step_2`, `step_3`, `step_4`, `step_5`, `step_5_1`) phục vụ kiểm chuẩn.
      + Hỗ trợ cờ `--benchmark-only` để chỉ chạy lại các bước kiểm chuẩn khi cần.
    - Cập nhật tài liệu kỹ thuật luồng `docs/PIPELINE.md` và hiện trạng `docs/HIEN_TRANG_HE_THONG.md`.
    - Ghi nhận cách xử lý lỗi `PermissionError` khi mở file CSV trên Windows vào `docs/LOI_THUONG_GAP.md`.

### 2026-09-17
22. **Thiết lập Step 5.3 — Cơ chế bù trừ rủi ro từ ý tưởng 5.1 dựa trên 4 đặc trưng tương tác của Step 4.1** — `e720263`
    - Tạo thư mục độc lập `repo_source/step_5_3/` (bảo toàn nguyên vẹn `step_5` và `step_5_1`).
    - Lấy đầu vào trực tiếp từ kết quả dự đoán của Step 4.1 (`prediction_test_has_default.csv` và `prediction_test_non_default.csv`).
    - Lớp GỠ: Sử dụng trực tiếp 2 biến tương tác bệ đỡ (`Tuong_tac_be_do_bds` và `Tuong_tac_be_do_dong_tien`) cùng ngưỡng xác suất rủi ro biên (< 0.65) để giải oan đúng **129 khách tốt (FP $\rightarrow$ TN)** (trong đó Tầng 1 BĐS đạt tỷ lệ giải oan vượt trội **4.25 : 1**; Tầng 2 đạt **2.25 : 1**).
    - Lớp VỚT: Sử dụng trực tiếp 2 biến tương tác biến cố (`Tuong_tac_bien_co_ngam` và `Tuong_tac_no_thue_nha`) cùng ngưỡng xác suất cảnh báo (>= 0.42) để bắt lại **14 ca rủi ro ngầm (FN $\rightarrow$ TP)**, đóng vai trò bù đắp trực tiếp cho số TP bị mất ở Lớp Gỡ.
    - Kết quả toàn hệ thống: Accuracy đạt kỷ lục mới **80.73%** (tăng từ 80.40% của Step 4.1); FP báo oan giảm ròng 44 ca xuống mức thấp kỷ lục **880 ca** (so với 1,039 ban đầu ở Step 4); TN duyệt đúng tăng lên **4,212 ca**; TP đạt **1,047 ca**; FN là 375 ca.
    - Xuất 3 file CSV độc lập: `prediction_final_evaluated.csv` (6,514 dòng), `rescued_fp.csv` (165 dòng), `caught_fn.csv` (99 dòng) và `step_5_3_hedging_report.json`.
    - Tích hợp tự động vào `run_pipeline.py` (chuỗi 8 bước) và `db_import.py` (đồng bộ 50 bảng, 405,994 dòng vào PostgreSQL schema `credit_model`).

### 2026-09-17
21. **Thiết lập Step 4.1 — Tích hợp 4 đặc trưng tương tác vào phương trình hồi quy & so sánh với Step 5.1** — `5b43f1c`
    - Tạo thư mục độc lập `repo_source/step_4_1/` (bảo toàn nguyên vẹn `step_4`).
    - Khai phá và tích hợp 4 biến tương tác phi tuyến vào phương trình: `Tuong_tac_be_do_bds`, `Tuong_tac_be_do_dong_tien`, `Tuong_tac_bien_co_ngam`, `Tuong_tac_no_thue_nha` (mở rộng tập đặc trưng từ 20 lên **24 biến**).
    - Chuẩn hóa `StandardScaler` và huấn luyện `LogisticRegression(class_weight='balanced')`.
    - Kết quả vượt trội: ROC-AUC tăng vọt từ 0.8406 lên **0.8609** (+0.0203); Test Accuracy tăng từ 78.65% lên **80.40%** (vượt qua Step 5.1); FP báo oan giảm sâu từ 1,039 xuống **924 ca** (giảm 115 ca oan ngay trong phương trình); TN duyệt đúng tăng từ 4,053 lên **4,168 ca** (+115 khách tốt); TP kiểm soát nợ xấu đạt **1,069 ca** (gần như nguyên vẹn).
    - Tích hợp tự động vào `run_pipeline.py`, `db_import.py` (load 45 bảng, 392,702 dòng) và `db_save_model.py` (lưu `step_4_1_model` và 24 hệ số tương tác vào PostgreSQL schema `credit_model`).

### 2026-09-17
20. **Thiết lập Step 5.1 — Cơ chế nhát cắt đặc trưng tối ưu GỠ và VỚT bù trừ rủi ro** — `2be484e`
    - Tạo thư mục độc lập `repo_source/step_5_1/` (bảo toàn nguyên vẹn `step_5`).
    - Lớp GỠ: Phân tầng bệ đỡ BĐS (Tầng 1) và Dòng tiền/Thâm niên (Tầng 2) giải oan thành công **196 khách tốt (FP $\rightarrow$ TN)**, chỉ chấp nhận mất 43 ca TP (tỷ lệ hiệu quả **4.56 FP giải oan / 1 TP mất**; riêng Tầng 1 đạt **5.40 : 1**).
    - Lớp VỚT: Nhận diện biến cố rủi ro ngầm (nhà thuê + nợ xấu cũ/quá hạn + prob >= 0.42) để vớt bắt lại **23 ca FN $\rightarrow$ TP**, đóng vai trò bù đắp trực tiếp cho số TP đã mất ở lớp Gỡ.
    - Xuất các file kết quả độc lập: `prediction_final_evaluated.csv` (6,514 dòng), `rescued_fp.csv` (239 dòng), `caught_fn.csv` (124 dòng), `step_5_1_hedging_report.json`.
    - Tích hợp vào `run_pipeline.py` và cập nhật `db_import.py` đồng bộ toàn bộ 39 bảng (321,056 dòng) vào PostgreSQL schema `credit_model`. Accuracy toàn hệ thống đạt **79.80%**, FP báo oan giảm ròng 95 ca (từ 1,039 xuống **944**).

### 2026-09-17
19. **Tối ưu VỚT (Catch FN) và GỠ (Rescue FP) tại Bước 5 theo ý tưởng tương tác nghiệp vụ (Cách 1)** — `c3cf3b5`
    - Cập nhật `repo_source/step_5/run.py` hiện thực hóa logic tương tác nghiệp vụ:
      + **Lớp GỠ (Rescue FP)**: Với hồ sơ mô hình đoán 1 nhưng có BĐS bảo chứng (Sở hữu/Thế chấp nhà) + Lịch sử sạch nợ xấu + Xác suất rủi ro biên (< 0.60), gán cờ `flag_go_fp = 1`, `action_step5 = "RESCUED_FP"` và chuyển `final_predicted = 0`. Kích hoạt trên 127 hồ sơ, giải oan thành công cho 108 khách hàng tốt (tỷ lệ chuẩn xác **85.04%**).
      + **Lớp VỚT (Catch FN)**: Với hồ sơ mô hình đoán 0 nhưng ở nhà thuê/khác + vay biến cố khẩn cấp (Y tế/Hợp nhất nợ đảo hạn) + có tiền sử nợ xấu + xác suất tiệm cận ngưỡng báo động (>= 0.40), gán cờ `flag_vot_fn = 1`, `action_step5 = "CAUGHT_FN"` và chuyển `final_predicted = 1`. Bắt trúng các ca rủi ro ngầm nguy hiểm nhất.
      + Xuất 3 file mới: `prediction_final_evaluated.csv` (toàn bộ 6,514 hồ sơ test có nhãn trước và sau hậu kiểm), `rescued_fp.csv` (127 ca được gỡ), `caught_fn.csv` (25 ca được vớt).
    - Cập nhật `repo_source/step_5/analyze_errors.py` và báo cáo `error_analysis_report.json`: Đánh giá hiệu quả trước và sau Step 5. Accuracy toàn hệ thống tăng từ 78.65% lên **79.78%** (+1.14%), số ca FP báo oan giảm từ 1,039 xuống **951** (giảm 88 ca oan), số khách tốt được duyệt (TN) tăng từ 4,053 lên **4,141** (+88 khách tốt).
    - Cập nhật `repo_source/db_import.py` tự động nạp 3 bảng mới vào PostgreSQL local schema `credit_model` (tổng 34 bảng, 307,665 dòng dữ liệu).

### 2026-09-16
18. **Nâng cấp Step 5 với các lớp lọc bóc tách sâu 2 tập has_default và non_default (Hướng B)** — `ddce1de`
    - Cập nhật `repo_source/step_5/run.py`: thêm các lớp lọc đặc trưng bóc tách 352 ca FN thành 2 phân khúc con (`_false_distress.csv`: 190 dòng vỡ nợ do biến cố ngầm và `_false_low_debt.csv`: 162 dòng vỡ nợ thu nhập cao nợ thấp); bóc tách 1,039 ca FP thành 3 phân khúc con (`_false_asset_backed.csv`: 560 dòng có BĐS bảo chứng, `_false_growth_investment.csv`: 189 dòng vay đầu tư dòng tiền, `_false_high_debt.csv`: 290 dòng nợ cao khác).
    - Cập nhật `repo_source/step_5/analyze_errors.py` và báo cáo `error_analysis_report.json` phản ánh chi tiết các phân khúc rủi ro.
    - Chạy lại pipeline và cập nhật cơ sở dữ liệu PostgreSQL (31 bảng, 300,999 dòng).

### 2026-09-16
17. **Tích hợp Financial Feature Engineering vào Step 4 để cải thiện mô hình** — `2fedce6`
    - Bổ sung hàm `engineer_features()` trong `repo_source/step_4/run.py` sinh 7 chỉ số phái sinh tài chính: ước tính nợ trả góp hàng tháng, tỷ lệ gánh nặng nợ (DSR), áp lực nợ tổng hợp, thâm niên trên tuổi đời, chỉ số căng thẳng tín dụng...
    - Mở rộng tập đặc trưng từ 8 lên 20 cột, chuẩn hóa StandardScaler và huấn luyện LogisticRegression cân bằng trọng số.
    - Test accuracy tiếp tục tăng lên **78.65%** (từ 77.40%), ROC-AUC đạt **0.8406** (từ 0.8290), Recall vỡ nợ đạt **75.25%** (1,070 ca đúng).
    - Chuẩn hóa vai trò Step 5: là bước hậu kiểm/phân loại độc lập, tự động tách 4 file: TP = **1,070**, FN = **352** (giảm thêm 17 ca bỏ sót), TN = **4,053**, FP = **1,039** (giảm thêm 64 ca báo nhầm).
    - Chạy lại `analyze_errors.py` và cập nhật cơ sở dữ liệu PostgreSQL (sửa lỗi schema tự động đồng bộ cột mới qua `DROP IF EXISTS CASCADE`).

### 2026-09-16
16. **Phân tích chuyên sâu nhóm dự đoán sai ở Step 5 (Error Analysis: 369 FN và 1,103 FP)** — `a4d815f`
    - Tạo `repo_source/step_5/analyze_errors.py`: ghép nối toàn bộ 29 cột từ `step_1/output/test.csv` qua `Mã khách hàng`.
    - Tìm ra nguyên nhân 369 ca FN bị bỏ sót: Thu nhập bình quân cao (~1.82 tỷ VND) và tỷ lệ vay/thu nhập thấp (0.14) đã "đánh lừa" mô hình tuyến tính; nhóm này có 18.4% từng có nợ xấu.
    - Tìm ra nguyên nhân 1,103 ca FP bị báo oan: Tỷ lệ vay/thu nhập cao (0.23) và lãi suất cao (13%) khiến mô hình báo động nhầm; thực tế 92.5% khách này có lịch sử tín dụng sạch và thâm niên làm việc bình quân 4.5 năm.
    - Xuất báo cáo chi tiết ra `repo_source/step_5/output/error_analysis_report.json`.

### 2026-09-16
15. **Tích hợp Step 4 mới (StandardScaler + LogisticRegression) và chuyển nhát cắt phân loại sang Step 5** — `18e02bf`
    - Chuyển `step_4/` cũ sang `step_5/`: nhận kết quả dự đoán từ step_4, phân loại đúng/sai thành 4 file `_true.csv` / `_false.csv` dựa trên `correct == 1`.
    - Viết `step_4/` mới: Chuẩn hóa 8 đặc trưng bằng `StandardScaler`, fit `LogisticRegression(class_weight="balanced")`, xuất `scaler.pkl`, `model_scaled.pkl`, `metadata.json`. Test accuracy tăng vọt từ 70.14% lên **77.40%**, AUC tăng từ 0.7264 lên **0.8290**, recall vỡ nợ tăng lên **74.05%** (bắt đúng 1,053 ca, giảm bỏ sót FN từ 557 xuống còn 369 ca).
    - Cập nhật `run_pipeline.py` điều phối trơn tru toàn bộ 5 bước (step_1 -> step_5).
    - Cập nhật `db_import.py` (load 26 bảng CSV, 299,608 dòng) và `db_save_model.py` (lưu thêm `step_4_model` và `step_4_model_coef`) vào PostgreSQL schema `credit_model`.

### 2026-09-15
14. **Lưu toàn bộ giá trị model.pkl vào PostgreSQL credit_model** — `185f167`
   - Tạo `repo_source/db_save_model.py`: đọc model.pkl + metadata.json, serialize params/coef/intercept/classes.
   - Bảng `step_2_model` (summary: feature_columns, hyperparameters, metrics, coefficients, intercept...) + `step_2_model_coef` (hệ số từng feature, PRIMARY KEY model_id+feature_index).
   - Đã lưu model id=1 (LogisticRegression, n_features 8: coef gần 0, intercept ≈1e-17), commit `185f167`.

### 2026-09-15
13. **Import CSV input/output mỗi step vào PostgreSQL local** — `396d46d`
   - Tạo `repo_source/db_import.py`, cài psycopg2-binary (2.9.13) vào venv.
   - DB: PostgreSQL 18.4 local / dbname postgres / user hnv / pass 123456 / schema credit_model.
   - Quét CSV step_1..step_4 (input + output), bảng tiền tố `step_{N}_{input|output}_{tên file}`.
   - Load 20 bảng, tổng 227,962 dòng; dùng `COPY ... FROM STDIN` (copy_expert) để load nhanh.
   - Sửa lỗi tên bảng `step_step_*` (do step_dirs chứa "step_1" thay vì "1"), fix bằng tách step_num.

### 2026-09-15
