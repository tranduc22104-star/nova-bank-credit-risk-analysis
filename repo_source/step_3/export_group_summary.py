import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(HERE, "output", "nhom_xac_suat_vo_no_4_muc.xlsx")
OUTPUT_PATH = os.path.join(HERE, "output", "tong_hop_nhom_xac_suat.csv")

PURPOSE = {0: "Cá nhân", 1: "Cải tạo nhà", 2: "Giáo dục", 3: "Hợp nhất nợ", 4: "Kinh doanh", 5: "Y tế"}
HOME = {0: "Khác", 1: "Sở hữu nhà", 2: "Thuê nhà", 3: "Thế chấp"}
EVER = {1: "Có", 0: "Không"}

NUM = [
    "Lãi suất khoản vay (%)",
    "Tỷ lệ khoản vay trên thu nhập",
    "Tỷ lệ tổng nợ trên thu nhập",
    "Thu nhập hàng năm (VND)",
    "Số tiền vay đề nghị (VND)",
]

RANGES = {
    "0-25%": (0.0, 0.25),
    "25-50%": (0.25, 0.50),
    "50-75%": (0.50, 0.75),
    "75-100%": (0.75, 1.01),
}

COLUMNS = [
    "Nhóm xác suất",
    "Số hồ sơ",
    "Tỷ lệ hồ sơ (%)",
    "Lãi suất TB (%)",
    "LTI TB",
    "DTI TB",
    "Thu nhập TB (tỷ VND)",
    "Số tiền vay TB (triệu VND)",
    "Sở hữu nhà ưu thế",
    "Mục đích vay ưu thế",
    "Tỷ lệ từng vỡ nợ (%)",
    "Tỷ lệ model đoán vỡ nợ (%)",
]


def main():
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"Không tìm thấy {INPUT_PATH}")

    xl = pd.ExcelFile(INPUT_PATH)
    if not os.path.exists(os.path.join(HERE, "output", "prediction_test_has_default.csv")):
        raise FileNotFoundError("Thiếu prediction_test_has_default.csv")
    full = pd.read_csv(os.path.join(HERE, "output", "prediction_test_has_default.csv"))
    total = len(full)

    rows = []
    for name, (lo, hi) in RANGES.items():
        df = xl.parse(name)
        p = (df["predicted"] == 1).mean() * 100
        ever = (df["Từng vỡ nợ trong hồ sơ tín dụng (Có/Không)"] == 1).mean() * 100
        top_purpose = df["Mục đích khoản vay"].value_counts().idxmax()
        top_home = df["Tình trạng sở hữu nhà"].value_counts().idxmax()
        rows.append([
            name,
            len(df),
            round(len(df) / total * 100, 2),
            round(df["Lãi suất khoản vay (%)"].mean(), 2),
            round(df["Tỷ lệ khoản vay trên thu nhập"].mean(), 3),
            round(df["Tỷ lệ tổng nợ trên thu nhập"].mean(), 3),
            round(df["Thu nhập hàng năm (VND)"].mean() / 1e9, 2),
            round(df["Số tiền vay đề nghị (VND)"].mean() / 1e6, 1),
            HOME[top_home],
            PURPOSE[top_purpose],
            round(ever, 1),
            round(p, 1),
        ])

    out = pd.DataFrame(rows, columns=COLUMNS)
    out.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
    print(out.to_string(index=False))
    print("Đã ghi:", os.path.abspath(OUTPUT_PATH))


if __name__ == "__main__":
    main()