import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(HERE, "output", "prediction_test_has_default.csv")
OUTPUT_PATH = os.path.join(HERE, "output", "nhom_xac_suat_vo_no_4_muc.xlsx")

PROB_COL = "prob_vỡ_nợ"
BUCKETS = [
    ("0-25%", 0.0, 0.25),
    ("25-50%", 0.25, 0.5),
    ("50-75%", 0.5, 0.75),
    ("75-100%", 0.75, 1.0),
]


def main():
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"Không tìm thấy {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH)
    if PROB_COL not in df.columns:
        raise ValueError(f"Thiếu cột {PROB_COL} trong {INPUT_PATH}")

    counts = []
    with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
        for name, lo, hi in BUCKETS:
            if name == "75-100%":
                sub = df[(df[PROB_COL] >= lo) & (df[PROB_COL] <= hi)]
            else:
                sub = df[(df[PROB_COL] >= lo) & (df[PROB_COL] < hi)]
            sub = sub.sort_values(PROB_COL, ascending=False)
            sub.to_excel(writer, sheet_name=name, index=False)
            counts.append((name, len(sub)))

    print(f"Tổng hồ sơ: {len(df)}")
    for name, n in counts:
        print(f"  {name}: {n} hồ sơ ({n / len(df) * 100:.2f}%)")
    print("Đã ghi:", os.path.abspath(OUTPUT_PATH))


if __name__ == "__main__":
    main()