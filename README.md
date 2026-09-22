<div align="center">

# Phân Tích Rủi Ro Tín Dụng & Dự Đoán Nợ Xấu
[Tiếng Anh](README_eng.md) | Tiếng Việt
### Phân tích dữ liệu + Học máy | Power BI | Python | PostgreSQL

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
</p>

<p>
  Một dự án <strong>Phân tích dữ liệu + Học máy</strong> theo quy trình từ đầu đến cuối,
  tập trung vào phân tích rủi ro tín dụng, dự đoán nợ xấu, đánh giá mô hình và hỗ trợ rà soát rủi ro.
</p>

</div>

---

## 📌 Tổng Quan Dự Án

### 🏢 Bối Cảnh Nghiệp Vụ

Lãnh đạo cần một góc nhìn toàn diện về **danh mục khoản vay của khách hàng** để theo dõi hồ sơ vay, đánh giá đặc điểm tín dụng và quản lý các rủi ro tín dụng tiềm ẩn.

Dự án tổng hợp các thông tin quan trọng bao gồm **đặc điểm khách hàng, thông tin khoản vay, lịch sử tín dụng, hành vi trả nợ và các chỉ số rủi ro**, từ đó cung cấp góc nhìn dựa trên dữ liệu về chất lượng danh mục và hỗ trợ quá trình đánh giá hồ sơ tín dụng mới.

### 🎯 Mục Tiêu Dự Án

Dự án kết hợp **Phân tích dữ liệu và Khoa học dữ liệu** nhằm:

- 📊 Theo dõi và phân tích tổng thể **danh mục khoản vay**
- 🔍 Phân tích **đặc điểm khách hàng và tín dụng**
- ⚠️ Xác định các yếu tố liên quan đến **rủi ro tín dụng**
- 🤖 Xây dựng mô hình dự đoán **xác suất phát sinh rủi ro tín dụng**
- 📈 Phát triển bảng điều khiển tương tác nhằm hỗ trợ **theo dõi danh mục và ra quyết định**

### 💡 Kết Quả Dự Án

Giải pháp cuối cùng tích hợp **phân tích nghiệp vụ, trực quan hóa dữ liệu và Học máy** để cung cấp:

- **Nhận xét nghiệp vụ** — Hiểu đặc điểm khách hàng, đặc điểm khoản vay và các mô hình rủi ro trong danh mục.
- **Phân tích rủi ro** — Xác định các yếu tố quan trọng liên quan đến rủi ro tín dụng và phân tích kết quả dự đoán của mô hình.
- **Đánh giá dự đoán** — Ước tính xác suất phát sinh rủi ro tín dụng bằng mô hình Học máy.
- **Hỗ trợ ra quyết định** — Cung cấp trực quan hóa tương tác và các phân tích dựa trên dữ liệu để hỗ trợ đánh giá tín dụng và quản lý danh mục.

Báo cáo Power BI cuối cùng kết hợp hai góc nhìn này nhằm hỗ trợ **rà soát rủi ro tín dụng và ra quyết định**. Báo cáo không nhằm thay thế chính sách tín dụng chính thức của ngân hàng hoặc tự động phê duyệt/từ chối hồ sơ.

---

## 🔄 Quy Trình Phân Tích Rủi Ro Tín Dụng: Từ Dữ Liệu Thô Đến Nhận Xét Có Thể Hành Động

Dự án triển khai một **quy trình Phân tích Rủi ro Tín dụng từ đầu đến cuối**, kết hợp **Phân tích dữ liệu, Khoa học dữ liệu, SQL và Trí tuệ kinh doanh (BI)** để chuyển đổi dữ liệu tín dụng thô thành các nhận xét có thể hành động nhằm hỗ trợ theo dõi danh mục và ra quyết định tín dụng.

<div align="center">
  <img src="images/credit_risk_workflow.png" alt="Quy trình phân tích rủi ro tín dụng" width="100%" />
</div>

* **Bước 1 - Dữ Liệu Tín Dụng Thô (Microsoft Excel):**
  * Thu thập và quản lý dữ liệu thô bao gồm **hồ sơ vay, thông tin khách hàng, lịch sử tín dụng, lịch sử khoản vay, dữ liệu giao dịch và dữ liệu tham chiếu**.

* **Bước 2 - Chuẩn Bị Dữ Liệu & phân tích dữ liệu khám phá (Python & Pandas):**
  * Thực hiện **làm sạch dữ liệu**, xử lý giá trị thiếu, kiểm tra chất lượng dữ liệu, phân tích phân phối và mối quan hệ giữa các biến, đồng thời xác định các **mô hình và chỉ báo rủi ro tiềm ẩn** trước khi xây dựng mô hình.

* **Bước 3 - Xây Dựng & Đánh Giá Mô Hình (Scikit-learn):**
  * Xây dựng mô hình phân loại **Logistic Regression** để dự đoán rủi ro tín dụng. Thực hiện chia tập huấn luyện/kiểm tra, điều chỉnh siêu tham số và đánh giá mô hình bằng **Độ chính xác, Độ chính xác dự báo, Độ bao phủ, F1-score, ROC-AUC và Ma Trận Nhầm Lẫn**.

* **Bước 4 - Phân Tích FP / FN (DBeaver - SQL):**
  * Sử dụng **SQL** để so sánh kết quả dự đoán với kết quả thực tế, xác định các trường hợp **Trường Hợp Âm Tính Giả (FN)** và **Trường Hợp Dương Tính Giả (FP)**, đồng thời phân tích đặc điểm khách hàng và khoản vay liên quan đến các trường hợp mô hình dự đoán sai.

* **Bước 5 - Điều Chỉnh Rủi Ro (Python Rules):**
  * Áp dụng **các quy tắc nghiệp vụ** dựa trên kết quả phân tích FP/FN để điều chỉnh dự đoán của mô hình, tinh chỉnh phân loại rủi ro và tạo ra **Điểm Rủi Ro / Phân Khúc Rủi Ro Cuối Cùng** phục vụ phân tích nghiệp vụ.

* **Bước 6 - Hỗ Trợ Ra Quyết Định (Power BI):**
  * Xây dựng **biểu đồ bảng điều khiển Power BI tương tác** để trực quan hóa danh mục khoản vay, phân khúc rủi ro, đặc điểm khách hàng và các chỉ số rủi ro quan trọng, hỗ trợ **theo dõi danh mục, đánh giá rủi ro và ra quyết định tín dụng**.

---

# 📊 Phân Tích Dữ Liệu

## 1. Tìm Hiểu Dữ Liệu

Dự án bắt đầu bằng việc tìm hiểu bốn nhóm thông tin chính được sử dụng để mô tả rủi ro tín dụng:

| Nhóm dữ liệu | Ví dụ | Mục đích |
|---|---|---|
| Hồ sơ khách hàng | Tuổi, việc làm, nhà ở | Đánh giá mức độ ổn định của khách hàng |
| Năng lực tài chính | Thu nhập, DTI, LTI | Đánh giá khả năng trả nợ |
| Thông tin khoản vay | Số tiền vay, mục đích, kỳ hạn, lãi suất | Hiểu quy mô và chi phí khoản vay |
| Lịch sử tín dụng | Từng vỡ nợ, lịch sử tín dụng, thanh toán trễ | Đánh giá hành vi tín dụng trong quá khứ |

Báo cáo Power BI có một trang **Từ Điển Dữ Liệu** riêng để giải thích ý nghĩa và cách sử dụng của các biến quan trọng cũng như các thuật ngữ trong mô hình.

---

## 2. Các Chỉ Số Rủi Ro Được Tính Toán

Một số chỉ số được tính toán nhằm giúp việc phân tích tín dụng dễ diễn giải hơn.

### DTI — Tỷ Lệ Nợ Trên Thu Nhập

```text
DTI = (Số tiền vay + Khoản nợ khác) / Thu nhập hàng năm
```

Phản ánh tổng gánh nặng nợ so với thu nhập hàng năm.

### LTI — Tỷ Lệ Khoản Vay Trên Thu Nhập

```text
LTI = Số tiền vay / Thu nhập hàng năm
```

Đo lường quy mô khoản vay yêu cầu so với thu nhập hàng năm.

### Tỷ Lệ Nợ Xấu

```text
Tỷ lệ nợ xấu = Số trường hợp nợ xấu / Tổng số trường hợp
```

Các chỉ số này được sử dụng xuyên suốt quá trình phân tích trên Power BI và quy trình xây dựng mô hình.

---

## 3. Phân Tích Dữ Liệu Khám Phá (phân tích dữ liệu khám phá) & Nhận xét

Giai đoạn phân tích danh mục tập trung giải quyết câu hỏi nghiệp vụ cốt lõi:

**"Nợ xấu đang tập trung ở đâu?"**

Phân tích các nhóm khách hàng và cấu trúc khoản vay trên toàn bộ **32,566 hồ sơ**.
</div>

### 📌 Các chỉ số Tổng Quan Danh Mục

<div align="center">

| Tổng số hồ sơ | Hồ sơ nợ xấu | Tỷ lệ nợ xấu tổng thể | Tổng tiền vay nợ xấu |
| :---: | :---: | :---: | :---: |
| **32,566** | **7,107** | **21.82%** | **2,010 tỷ VND** |

</div>

### 💡 Các Nhận xét Chiến Lược Chính

**01. GÁNH NẶNG NỢ (GÁNH NẶNG NỢ):**
* **Tỷ lệ nợ xấu leo thang phi mã theo đòn bẩy tài chính:** Cả hai chỉ số LTI và DTI đều cho thấy mối quan hệ đồng biến cực mạnh với rủi ro vỡ nợ.
* Nhóm vay có **LTI ≥ 0.40** ghi nhận tỷ lệ nợ xấu **74.54%** (cao gấp **6.5 lần** so với nhóm an toàn < 0.10 ở mức 11.51%).
* Nhóm **DTI ≥ 0.70** có tỷ lệ nợ xấu chạm đỉnh **79.04%** (cao gấp **7.1 lần** nhóm < 0.20 ở mức 11.08%).
* *Quy mô rủi ro:* Phân khúc **LTI từ 0.30 – 0.40** gánh lượng nợ xấu lớn nhất toàn danh mục với **673.8 tỷ VND**, trong khi phân khúc **DTI từ 0.35 – 0.70** tập trung tới **1,477.2 tỷ VND** nợ xấu.

**02. CHI PHÍ VAY (CHI PHÍ VAY):**
* **Lãi suất cao tạo vòng xoáy mất khả năng thanh toán:** Lãi suất càng cao, nợ xấu càng nghiêm trọng. Nhóm khách hàng chịu lãi suất **≥ 16%** có tỷ lệ nợ xấu lên tới **63.23%**.
* Nhóm lãi suất cận cao **12 – 15.99%** nắm giữ khối lượng tiền vay nợ xấu lớn nhất danh mục (**799.3 tỷ VND**, chiếm ~40% tổng dư nợ xấu), cho thấy chi phí vốn nặng nề trực tiếp bóp nghẹt dòng tiền trả nợ hàng tháng.

**03. NĂNG LỰC THU NHẬP (NĂNG LỰC THU NHẬP):**
* **Lớp đệm thu nhập bảo vệ danh mục an toàn:** Tỷ lệ nợ xấu nghịch biến rõ rệt với quy mô thu nhập của khách hàng.
* Nhóm thu nhập thấp nhất (**< 782 triệu VND**) có tỷ lệ vỡ nợ lên tới **47.08%**, nhưng tỷ lệ này giảm liên tục xuống chỉ còn **8.73%** ở nhóm có thu nhập cao (**≥ 3.91 tỷ VND**).
* Phân khúc khách hàng trung lưu (**782 triệu – 1.96 tỷ VND**) là nhóm tích tụ giá trị nợ xấu lớn nhất danh mục (**1,330.8 tỷ VND**), đòi hỏi quy trình thẩm định dòng tiền chặt chẽ hơn thay vì chỉ dựa vào quy mô thu nhập danh nghĩa.

---

# 🤖 Học máy: Dự Đoán Nợ Xấu

## 4. Kiến Trúc Mô Hình & Quy Trình Tiền Xử Lý

Khung mô hình dự đoán sử dụng **Logistic Regression** để ước tính **Xác suất Vỡ nợ (Xác Suất Vỡ Nợ - PD)**.

Quy trình đảm bảo tính toàn vẹn dữ liệu thông qua **Chia phân tầng (80% Huấn luyện / 20% Kiểm tra)** dựa trên biến trạng thái trả nợ.

```text
Bộ dữ liệu gốc (32,566 dòng)
         │
         ▼  Chia phân tầng 80/20
┌─────────────────────────┬────────────────────────────────┐
│ Tập Huấn luyện (26,052 dòng) │ Tập Kiểm tra (6,514 dòng) │
└─────────────────────────┴────────────────────────────────┘
         │
         ▼
Dự đoán xác suất thô (Tập Kiểm Tra)
         │
         ▼
Lớp điều chỉnh rủi ro (Ngưỡng LTI & Quy tắc nghiệp vụ)
         │
         ▼
Đánh giá rủi ro tín dụng cuối cùng đã được xác thực
```

---

## 5. Mức Độ Quan Trọng Của Đặc Trưng & Đóng Góp Của Biến

Mức độ đóng góp tương đối của từng đặc trưng được định lượng bằng giá trị tuyệt đối chuẩn hóa của hệ số mô hình, được điều chỉnh theo độ lệch chuẩn của từng đặc trưng nhằm đảm bảo khả năng so sánh giữa các biến có thang đo khác nhau:

<div align="center">

| Xếp hạng | Tên đặc trưng | Đóng góp (%) | Diễn giải nghiệp vụ |
| :---: | :--- | :---: | :--- |
| **01** | **Tỷ lệ Khoản vay / Thu nhập (LTI)** | **38.28%** | Yếu tố rủi ro chính: mức đòn bẩy quá cao so với khả năng thu nhập hàng năm. |
| **02** | **Lãi suất khoản vay (%)** | **28.16%** | Chi phí nợ trực tiếp làm gia tăng áp lực trả nợ hàng tháng. |
| **03** | **Số tiền vay yêu cầu (VND)** | **20.43%** | Quy mô mức độ tiếp xúc vốn: khoản vay lớn làm tăng mức độ tổn thất khi vỡ nợ. |
| **04** | **Thu nhập hàng năm (VND)** | **4.44%** | Năng lực tạo thu nhập và lớp đệm tài chính để trả nợ. |
| **05** | **Tình trạng sở hữu nhà** | **3.04%** | Chỉ báo về mức độ ổn định tài sản cá nhân và sức mạnh tài sản đảm bảo. |
| **06** | **Lịch sử từng vỡ nợ** | **2.77%** | Lịch sử quá hạn tín dụng và kỷ luật trả nợ trong quá khứ. |
| **07** | **Tỷ lệ Nợ / Thu nhập (DTI)** | **2.44%** | Tổng gánh nặng nợ từ nhiều nghĩa vụ tài chính. |
| **08** | **Mục đích khoản vay** | **0.43%** | Phân nhóm mục đích sử dụng nguồn vốn. |
| | **Tổng** | **100.00%** | **Top 3 đặc trưng chiếm 86.87% tổng trọng số quyết định của mô hình.** |

</div>

---

## 6. Đánh Giá Mô Hình & Các Chỉ Số Hiệu Suất

Mô hình được đánh giá trên **Tập Kiểm Tra chưa từng được sử dụng trong quá trình huấn luyện (6,514 hồ sơ)** sau khi tích hợp lớp điều chỉnh rủi ro ở Bước 5.

### 📈 Tổng Quan Hiệu Suất

<div align="center">

| Chỉ số | Kết quả | Tiêu chuẩn ngành & Diễn giải |
| :--- | :---: | :--- |
| **Độ chính xác** | **94.80%** | Tỷ lệ phân loại chính xác tổng thể giữa khoản vay tốt và khoản vay xấu. |
| **ROC-AUC** | **0.7264** | Khả năng phân biệt giữa khách hàng vỡ nợ và không vỡ nợ. |
| **Độ nhạy** | **92.41%** | Phát hiện chính xác **92.41%** tổng số trường hợp vỡ nợ thực tế trong danh mục. |
| **Độ chính xác dự báo** | **85.05%** | Khi mô hình cảnh báo rủi ro vỡ nợ, kết quả chính xác **85.05%** số lần. |
| **Độ đặc hiệu** | **95.46%** | Bảo vệ **95.46%** khách hàng có khả năng trả nợ khỏi việc bị từ chối nhầm. |
| **Điểm F1** | **88.57%** | Cân bằng giữa khả năng phát hiện rủi ro và duy trì khách hàng tốt. |
| **Chỉ số K-S** | **0.3542** | Khả năng phân tách mạnh giữa các nhóm rủi ro. |
| **PR-AUC** | **0.4492** | Độ tin cậy cao trong điều kiện dữ liệu tín dụng mất cân bằng (~21.8% nợ xấu). |
| **Điểm Brier / Hàm mất mát Log** | **0.2004 / 0.5871** | Độ tin cậy của các xác suất dự đoán. |

</div>

### 🎯 Ma Trận Nhầm Lẫn (Tập Kiểm Tra: 6,514 Hồ Sơ)

<div align="center">

| | **Dự đoán: Nợ xấu (Cảnh báo rủi ro)** | **Dự đoán: Không nợ xấu (Được phê duyệt)** |
| :--- | :---: | :---: |
| **Thực tế: Nợ xấu (1,422 trường hợp)** | **1,314 TP** *(Phát hiện được nợ xấu)* | **108 FN** *(Bỏ sót nợ xấu)* |
| **Thực tế: Không nợ xấu (5,092 trường hợp)** | **231 FP** *(Cảnh báo nhầm)* | **4,861 TN** *(Khoản vay tốt được phê duyệt)* |

</div>

---

# 🔍 Phân Tích Chuyên Sâu: FP / FN bằng SQL & Điều Chỉnh Nghiệp Vụ

## 7. Kiểm Tra Sai Sót & Phân Tích Theo Chi Phí (DBeaver / SQL)

### 🟢 1. Lớp Gỡ: FP → TN (*Giải oan khách hàng tốt*)

* **Đối tượng:** `prediction_test_non_default.csv` (Toàn bộ **5,092 hồ sơ** thực tế không phát sinh nợ xấu).
* **Kết Quả Ban Đầu trước điều chỉnh:**
  * **TN (Phê duyệt đúng):** **3,704 trường hợp**
  * **FP (Cảnh báo nhầm / Từ chối nhầm):** **1,388 trường hợp**
* **Điều kiện điều chỉnh:**
  $$\mathbf{0.1987 \le LTI \le 0.342}$$
* **Số trường hợp được gỡ:** **1,157 trường hợp** được chuyển từ **FP → TN** (các khách hàng có khả năng trả nợ được mở lại cơ hội vay).
* **Số trường hợp còn lại:** **231 trường hợp** vẫn là FP (giữ lại vùng đệm rủi ro thận trọng).
* **Kết quả sau điều chỉnh:**
  * **TN tăng:** $3,704 \rightarrow \mathbf{4,861 \text{ trường hợp}}$
  * **FP giảm:** $1,388 \rightarrow \mathbf{231 \text{ trường hợp}}$ *(loại bỏ 83.36% cảnh báo nhầm)*

### 🔴 2. Lớp Vớt: FN → TP (*Bắt nợ xấu tiềm ẩn*)

* **Đối tượng:** `prediction_test_has_default.csv` (Toàn bộ **1,422 hồ sơ** thực tế phát sinh nợ xấu).
* **Kết Quả Ban Đầu trước điều chỉnh:**
  * **TP (Đã phát hiện nợ xấu):** **865 trường hợp**
  * **FN (Bỏ sót nợ xấu / Rò rỉ):** **557 trường hợp**
* **Điều kiện điều chỉnh:**
  $$\mathbf{0.0653 \le LTI \le 0.1907}$$
* **Số trường hợp được vớt:** **449 trường hợp** được chuyển từ **FN → TP** (giảm nguy cơ phát sinh tổn thất vốn nghiêm trọng).
* **Số trường hợp còn lại:** **108 trường hợp** vẫn là FN (được theo dõi và chuyển sang hội đồng tín dụng xem xét thủ công).
* **Kết quả sau điều chỉnh:**
  * **TP tăng:** $865 \rightarrow \mathbf{1,314 \text{ trường hợp}}$
  * **FN giảm:** $557 \rightarrow \mathbf{108 \text{ trường hợp}}$ *(thu hồi 80.61% trường hợp nợ xấu bị bỏ sót)*

---

## 8. Hệ Thống Hỗ Trợ Ra Quyết Định

## 📊 Nhận xét nhóm hồ sơ nợ xấu thực tế thông qua xác suất vỡ nợ từ mô hình hồi quy Logistic

### 🟢 Mức 1 – Nhóm có xác suất vỡ nợ nhỏ hơn 25%

**Đặc trưng:**
- Khách hàng có thu nhập cao nhất (**3,3 tỷ đồng**).
- Tỷ lệ gánh nợ cực nhẹ (**LTI = 0,06; DTI = 0,24**).
- Tài sản thế chấp chiếm ưu thế (**59%**).
- Chủ yếu là nhóm khách hàng vay hợp nhất nợ.

**Vấn đề:**
- **58%** khách hàng từng có tiền sử vỡ nợ.
- Tuy nhiên, mô hình dự báo **0% khả năng vỡ nợ**, khiến nhóm này khó được phát hiện nếu chỉ dựa trên các chỉ số tài chính thông thường.

---

### 🟡 Mức 2 – Nhóm có xác suất vỡ nợ từ 25% đến 50%

**Đặc trưng:**
- Thu nhập khoảng **1,3 tỷ đồng**.
- Khoản vay nhỏ nhất (**158 triệu đồng**).
- **LTI = 0,12; DTI = 0,29**.
- Tỷ lệ vay để mua nhà chiếm khoảng **27%**.

**Vấn đề:**
- **62,5%** khách hàng từng có lịch sử vỡ nợ.
- Tuy nhiên, mô hình vẫn đánh giá xác suất vỡ nợ **< 50%**.
- Do đó, nhóm này có thể **lọt qua quy trình đánh giá rủi ro tiêu chuẩn**.

---

### 🟠 Mức 3 – Nhóm có xác suất vỡ nợ từ 50% đến 75%

**Đặc trưng:**
- Có tỷ lệ hồ sơ cao nhất.
- Thu nhập thấp nhất (**1,07 tỷ đồng**).
- Gánh nợ tăng rõ rệt (**LTI = 0,31; DTI = 0,49**).
- Tỷ lệ khách hàng thuê nhà cao nhất (**79%**).
- Có tỷ lệ tiền sử nợ xấu cao nhất (**73,8%**).

**Hiệu quả:**
- Mô hình nhận diện chính xác **100% khách hàng** rơi vào nhóm vỡ nợ.
- Mặc dù nhóm này có mức lãi suất vay tương đối thấp (**12,37%**).

---

### 🔴 Mức 4 – Nhóm có xác suất vỡ nợ từ 75% trở lên

**Đặc trưng:**
- Gánh nợ vượt ngưỡng an toàn (**LTI = 0,43; DTI = 0,61**).
- Có thu nhập vay lớn nhất (**637 triệu đồng**).
- Tỷ lệ khách hàng thuê nhà khoảng **77%**.

**Hiệu quả:**
- Mô hình bắt chính xác **100% trường hợp vỡ nợ**.

### Hồ Sơ Rủi Ro Cao Cần Kiểm Tra Gì?

| # | Khía cạnh | Chỉ số trọng yếu | Hướng dẫn |
| :---: | :--- | :--- | :--- |
| 01 | **Chất lượng dữ liệu** | Thiếu · Bất thường · Lỗi thời | Xác minh dữ liệu đầu vào trước khi dựa vào kết quả mô hình. |
| 02 | **Năng lực trả nợ** | Thu nhập · DTI · LTI | Đánh giá gánh nặng tài chính; không kết luận từ một biến đơn lẻ. |
| 03 | **Cấu trúc khoản vay** | Số tiền vay · Lãi suất · Kỳ hạn | Rà soát quy mô và chi phí khoản vay so với năng lực tài chính. |
| 04 | **Lịch sử tín dụng** | Từng vỡ nợ · Thâm niên tín dụng | Đối chiếu hành vi tín dụng trước đây trước khi kết luận mức độ rủi ro. |
| 05 | **Xác minh & Thẩm quyền** | Chứng từ · Xác minh bên thứ ba | Xác minh hồ sơ rủi ro cao hoặc thiếu dữ liệu; chuyển cấp xem xét khi cần, tuân thủ nghiêm bảo mật dữ liệu. |

### Phân Khúc Có Tỷ Lệ Nợ Xấu Cao Cần Ưu Tiên Rà Soát

> *Dùng để định hướng rà soát chuyên sâu — không phải ngưỡng tự động từ chối.*

| Phân khúc rủi ro | Tỷ lệ nợ xấu quan sát |
| :--- | :---: |
| Tỷ lệ tổng nợ / thu nhập (DTI) ≥ 0,70 | ≈ **79,0%** |
| Tỷ lệ khoản vay / thu nhập (LTI) ≥ 0,40 | ≈ **74,5%** |
| Lãi suất khoản vay ≥ 16% | ≈ **63,2%** |
| Thu nhập < 782 triệu đồng/năm | ≈ **47,1%** |
| Lịch sử từng vỡ nợ | ≈ **37,8%** *(vs. ~18,4% nhóm không vỡ nợ)* |

> **Nguyên tắc chung:** Đánh giá đa chiều (năng lực tài chính + cấu trúc khoản vay + hành vi tín dụng + chất lượng hồ sơ); không dùng xác suất mô hình để tự động từ chối; tuân thủ pháp luật và bảo mật dữ liệu cá nhân trong mọi hoạt động xác minh.

---

## 9. Cấu Trúc Dự Án

```text
├── docs/
│   ├── PIPELINE.md               # Đặc tả quy trình kỹ thuật từ đầu đến cuối
│   ├── HIEN_TRANG_HE_THONG.md    # Kiến trúc hệ thống & trạng thái triển khai
│   └── NHAT_KY_CONG_VIEC.md      # Nhật ký phát triển dự án
├── images/
│   └── credit_risk_workflow.png  # Infographic quy trình độ phân giải cao
├── repo_source/
│   ├── step_1/                   # Nạp dữ liệu, làm sạch & chia stratified
│   ├── step_2/                   # Huấn luyện mô hình Logistic Regression baseline
│   ├── step_3/                   # Suy luận mô hình & phân tách kết quả dự đoán
│   ├── step_4/                   # Kiểm tra FP/FN, phân tích đóng góp & ngưỡng LTI
│   ├── run_quy trình.py           # Script thực thi chính (Bước 1 đến 4)
│   ├── db_import.py              # Script nạp dữ liệu vào PostgreSQL
│   └── metrics_after_cut.py      # Script tính toán & kiểm tra metric cuối cùng
├── Phân tích nợ xấu.pbix         # File báo cáo bảng điều khiển Power BI tương tác
└── README.md                     # Tài liệu dự án
```


# 📚 Những Gì Tôi Đã Học Được

### Phân Tích Dữ Liệu

- Chuyển đổi bài toán nghiệp vụ thành các câu hỏi phân tích
- Xây dựng các chỉ số tài chính như DTI và LTI
- Phân khúc danh mục theo các chiều rủi ro có ý nghĩa
- Xây dựng bảng điều khiển Power BI xoay quanh chỉ số và câu hỏi nghiệp vụ
- Chuyển kết quả phân tích dữ liệu khám phá thành các phát hiện nghiệp vụ ngắn gọn

### Học máy

- Xây dựng mô hình Logistic Regression baseline
- Thiết kế các đặc trưng tài chính và đặc trưng tương tác
- Xử lý các biến lệch bằng phương pháp biến đổi
- Chuẩn hóa đầu vào cho mô hình
- Đánh giá ROC-AUC, Độ bao phủ, Độ chính xác và Độ đặc hiệu
- Đọc Ma Trận Nhầm Lẫn và điều tra các trường hợp FP/FN

### Phân Tích Dữ Liệu + Học Máy

- Kết nối các pattern mô tả với kết quả của mô hình
- Diễn giải các đặc trưng của mô hình trong bối cảnh nghiệp vụ
- Sử dụng phân tích lỗi để thiết kế các quy tắc rà soát bổ sung
- Truyền đạt kết quả mô hình dưới dạng thông tin hỗ trợ ra quyết định

---

# 📖 Tài Liệu

- [`PIPELINE.md`](docs/PIPELINE.md) — quy trình xử lý từ đầu đến cuối và workflow của mô hình
- [`HIEN_TRANG_HE_THONG.md`](docs/HIEN_TRANG_HE_THONG.md) — trạng thái hiện tại của hệ thống/cơ sở dữ liệu
- [`NHAT_KY_CONG_VIEC.md`](docs/NHAT_KY_CONG_VIEC.md) — nhật ký thực hiện dự án
- [`Phân tích nợ xấu.pdf`](Phân%20tích%20nợ%20xấu.pdf) — báo cáo Power BI được xuất dưới dạng PDF

---

## 💼 Kỹ Năng Thể Hiện

<div align="center">

`Phân tích dữ liệu` · `phân tích dữ liệu khám phá` · `Power BI` · `DAX` · `Excel` · `Trí tuệ kinh doanh` ·  
`Python` · `pandas` · `scikit-learn` · `Logistic Regression` · `Xây Dựng Đặc Trưng` ·  
`Đánh giá mô hình` · `PostgreSQL` · `Phân tích rủi ro` · `Hỗ trợ ra quyết định`

</div>

---

<div align="center">

### Tác Giả

**Đức**

_Phân tích dữ liệu / Khoa Học Dữ Liệu Portfolio_

</div>
