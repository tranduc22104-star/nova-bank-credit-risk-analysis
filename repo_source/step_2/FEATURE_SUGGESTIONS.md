# Đề xuất biến đặc trưng cho huấn luyện

> Ngày: 2026-09-15 | Dataset: Credit Risk Dataset Chính.xlsx (32,566 dòng)
> Target: `Trạng thái trả nợ (0 = không vỡ nợ, 1 = vỡ nợ)` — tỷ lệ 78.2% / 21.8%
> Cập nhật: **LOẠI `Hạng tín dụng khoản vay`** — biến chỉ tồn tại SAU khi khoản vay được thẩm định/hình thành, không có sẵn tại thời điểm duyệt hồ sơ (tránh data leakage).

## 1. Kết quả phân tích tương quan với target (train)

| # | Biến | Pearson | Đánh giá |
|---|---|---|---|
| 1 | Tỷ lệ khoản vay trên thu nhập | **+0.386** | Mạnh nhất |
| 2 | Tỷ lệ thu nhập dành cho trả nợ | **+0.380** | Mạnh |
| ~~3~~ | ~~Hạng tín dụng khoản vay~~ | ~~+0.372~~ | ~~Mạnh~~ — **LOẠI** (leakage: tồn tại sau khi khoản vay hình thành) |
| 4 | Tỷ lệ tổng nợ trên thu nhập | +0.321 | Khá |
| 5 | Lãi suất khoản vay (%) | +0.317 | Khá |
| 6 | Từng vỡ nợ trong hồ sơ tín dụng (Có/Không) | -0.175 | Trung bình |
| 7 | Thu nhập hàng năm (VND) | -0.172 | Trung bình |
| 8 | Khoản nợ khác (VND) | -0.136 | Yếu |
| 9 | Tình trạng sở hữu nhà | -0.103 | Yếu |
| 10 | Số tiền vay đề nghị (VND) | +0.102 | Yếu |
| 11 | Các biến còn lại (Tuổi, Học vấn, Giới tính, Địa lý...) | < 0.09 | Không có sức dự đoán |

## 2. Vấn đề đa cộng tuyến (multicollinearity)

Các cặp biến gần như giống hệt — **chỉ giữ 1 trong cặp**:

| Cặp biến | Hệ số | Xử lý đề xuất |
|---|---|---|
| Tỷ lệ thu nhập dành cho trả nợ ↔ Tỷ lệ khoản vay trên thu nhập | **0.999** | Giữ 1, bỏ biến kia (đầy đủ thông tin trùng lặp) |
| Hạng tín dụng ↔ Lãi suất khoản vay | 0.891 | Hạng tín dụng đã LOẠI do leakage → giữ Lãi suất |
| Tuổi ↔ Thời gian lịch sử tín dụng | 0.878 | Giữ 1 |
| Thu nhập ↔ Khoản nợ khác | 0.851 | Giữ Thu nhập (ý nghĩa hơn) |
| Tỷ lệ khoản vay trên thu nhập ↔ Tỷ lệ tổng nợ | 0.829 | Có thể chọn 1 |
| Vĩ độ ↔ Kinh độ, Quốc gia ↔ Kinh độ | 0.72–0.78 | Bỏ nhóm địa lý |

## 3. Phân tích nhóm categorical (default rate theo từng nhóm)

| Biến | Chênh lệch khoảng cách class | Kết luận |
|---|---|---|
| **Tình trạng sở hữu nhà** | Thuê=31.6% / Sở hữu=7.2% | **Giữ** |
| **Từng vỡ nợ** | Có=37.4% / Không=18.5% | **Giữ** |
| **Mục đích khoản vay** | Hợp nhất nợ=28.6% / Kinh doanh=15% | Giữ (nếu giữ ít biến) |
| ~~Hạng tín dụng khoản vay~~ | ~~A=9.9% → G=98%~~ | ~~Giữ~~ — **LOẠI do leakage** |
| Giới tính | 22.1% / 21.6% | Bỏ |
| Tình trạng hôn nhân | ~21.7% đồng đều | Bỏ |
| Trình độ học vấn | ~22% đồng đều | Bỏ |
| Quốc gia/Tỉnh/Thành phố cư trú | ~21–22% đồng đều | **Bỏ toàn bộ nhóm địa lý** |
| Loại hình việc làm | ~21–23% đồng đều | Bỏ |

## 4. Đề xuất biến đưa vào huấn luyện

### Nhóm A — Danh sách đặc trưng đề xuất (KHÔNG được trùng lặp)

| # | Biến | Lý do |
|---|---|---|
| 1 | **Lãi suất khoản vay (%)** | +0.317, phản ánh rủi ro được định giá |
| 2 | **Tỷ lệ khoản vay trên thu nhập** | +0.386, biến mạnh nhất (đại diện tỷ lệ nợ) |
| 3 | **Tỷ lệ tổng nợ trên thu nhập** | +0.321 (giữ được nhờ khác hẳn biến #2) |
| 4 | **Thu nhập hàng năm (VND)** | -0.172, năng lực trả nợ |
| 5 | **Tình trạng sở hữu nhà** | Phân cách 31.6% vs 7.2% |
| 6 | **Từng vỡ nợ trong hồ sơ tín dụng (Có/Không)** | Gấp ~2 lần rủi ro |
| 7 | **Số tiền vay đề nghị (VND)** | +0.102, quy mô khoản vay |
| 8 | **Mục đích khoản vay** | Chênh lệch 28.6% vs 15% |

### Nhóm B — Biến nên LOẠI

- `Mã khách hàng` (đã bỏ ở step_1 — ID vô nghĩa)
- **`Hạng tín dụng khoản vay`** — **LOẠI vì data leakage**: đây là kết quả xếp loại tín dụng SAU khi khoản vay được thẩm định/hình thành, KHÔNG có sẵn tại thời điểm duyệt hồ sơ, chỉ có thông tin khách hàng là chính.
- **Nhóm địa lý**: Quốc gia, Tỉnh/Bang, Thành phố, Vĩ độ, Kinh độ (đồng đều ~22%)
- **Nhân khẩu vô nghĩa**: Giới tính, Tình trạng hôn nhân, Trình độ học vấn, Loại hình việc làm
- **Giảm đa cộng tuyến**: Tỷ lệ thu nhập dành cho trả nợ (trùng 0.999 với Tỷ lệ khoản vay trên thu nhập), Khoản nợ khác (trùng Thu nhập), Thời gian lịch sử tín dụng (trùng Tuổi)
- Số lần quá hạn, Số tài khoản tín dụng, Thời hạn vay, Tuổi, Thâm niên (tương quan ≤ 0.1)

## 5. Lưu ý quan trọng về mô hình

1. **Target là binary (0/1)** — Linear Regression *có thể chạy* nhưng kém phù hợp:
   - Dự đoán có thể ra ngoài [0, 1]
   - R² sẽ thấp (đã thấy 0.566 khi test nhanh trên dữ liệu tổng hợp)
   - **Khuyến nghị thay Logistic Regression / mô hình phân loại** để có xác suất ra kèm threshold
2. Nếu bắt buộc dùng Linear Regression: cân nhắc **chuẩn hóa/scale** các biến lớn (thu nhập ~46 tỷ, số tiền vay ~) để tránh hệ số khổng lồ.
3. **Cân bằng lớp (class imbalance) 78/22**: cân nhắc `class_weight`, hoặc giữ stratify như step_1 đã làm.

## 6. Cách dùng danh sách này trong step_2

Mở `run.py` trong step_2 và đặt:

```python
FEATURE_COLUMNS = [
    "Lãi suất khoản vay (%)",
    "Tỷ lệ khoản vay trên thu nhập",
    "Tỷ lệ tổng nợ trên thu nhập",
    "Thu nhập hàng năm (VND)",
    "Tình trạng sở hữu nhà",
    "Từng vỡ nợ trong hồ sơ tín dụng (Có/Không)",
    "Số tiền vay đề nghị (VND)",
    "Mục đích khoản vay",
]
```

> **LƯU Ý**: KHÔNG đưa `Hạng tín dụng khoản vay` vào danh sách — biến này chỉ tồn tại sau khi khoản vay được thẩm định, dùng nó sẽ dẫn đến **data leakage** (mô hình học được thông tin tương lai, kết quả đánh giá sẽ quá lạc quan và không ứng dụng được thực tế).
> Nếu để trống (`[]`), step_2 sẽ tự dùng **tất cả cột** trừ target — kết quả sẽ bị giảm chất lượng do biến nhiễu và đa cộng tuyến.

## 7. Phụ lục — Default rate chi tiết nhóm chính

> Bảng dưới chỉ để tham khảo đặc trưng dữ liệu. `Hạng tín dụng khoản vay` **KHÔNG được dùng cho huấn luyện** (data leakage), nên default rate theo hạng tín dụng chỉ mang tính khảo sát.

| Hạng tín dụng | Default rate | | Tình trạng nhà | Default rate |
|---|---|---|---|---|
| A | 9.9% | | Sở hữu nhà | 7.2% |
| B | 16.4% | | Thế chấp | 12.5% |
| C | 20.5% | | Khác | 30.6% |
| D | 59.0% | | Thuê nhà | 31.6% |
| E | 64.3% | | | |
| F | 70.0% | | | |
| G | 98.0% | | | |

| Từng vỡ nợ | Default rate | | Mục đích vay | Default rate |
|---|---|---|---|---|
| Không | 18.5% | | Kinh doanh | 15.0% |
| Có | 37.4% | | Giáo dục | 17.5% |
| | | | Cá nhân | 19.6% |
| | | | Y tế | 26.3% |
| | | | Cải tạo nhà | 26.5% |
| | | | Hợp nhất nợ | 28.6% |