import argparse
import glob
import json
import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(HERE, "input")
OUTPUT_DIR = os.path.join(HERE, "output")

TRAIN_RATIO = 0.8
RANDOM_STATE = 42
SHEET_NAME = "Dữ liệu rủi ro tín dụng"
TARGET_COLUMN = "Trạng thái trả nợ (0 = không vỡ nợ, 1 = vỡ nợ)"
ID_COLUMNS = ["Mã khách hàng"]


def read_input_files(input_dir):
    xlsx_files = glob.glob(os.path.join(input_dir, "*.xlsx")) + glob.glob(
        os.path.join(input_dir, "*.xls")
    )
    if not xlsx_files:
        raise FileNotFoundError(f"Khong tim thay file excel trong {input_dir}")
    frames = []
    encoders = {}
    for path in xlsx_files:
        df = pd.read_excel(path, sheet_name=SHEET_NAME)
        frames.append(df)
    if not frames:
        raise ValueError("Khong doc duoc du lieu tu cac file excel")
    df = pd.concat(frames, ignore_index=True)
    df = df.drop_duplicates()
    return df


def main():
    parser = argparse.ArgumentParser(description="Step 1: boc tach excel -> train/test csv")
    parser.add_argument("--train-ratio", type=float, default=TRAIN_RATIO)
    parser.add_argument("--random-state", type=int, default=RANDOM_STATE)
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Doc du lieu excel tu {INPUT_DIR}...")
    df = read_input_files(INPUT_DIR)
    print(f"Tong so dong: {len(df)}")

    for col in ID_COLUMNS:
        if col in df.columns:
            print(f"  Giữ cột ID: {col} (để truy vết kết quả dự đoán)")

    encoders = {}
    cat_cols = [
        c for c in df.select_dtypes(include=["object", "string"]).columns.tolist()
        if c not in ID_COLUMNS
    ]
    print(f"  Categorical columns ({len(cat_cols)}): {cat_cols}")
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le.classes_.tolist()

    encoders_path = os.path.join(OUTPUT_DIR, "label_encoders.json")
    with open(encoders_path, "w", encoding="utf-8") as f:
        json.dump(encoders, f, ensure_ascii=False, indent=2)
    print(f"  Da luu label encoders: {encoders_path}")

    target = TARGET_COLUMN
    feature_cols = [c for c in df.columns if c != target]
    print(f"  Target: {target}")
    print(f"  Features ({len(feature_cols)}): {feature_cols[:5]}...")

    train, test = train_test_split(
        df, train_size=args.train_ratio, random_state=args.random_state, shuffle=True,
        stratify=df[target] if df[target].nunique() <= 20 else None,
    )

    train_path = os.path.join(OUTPUT_DIR, "train.csv")
    test_path = os.path.join(OUTPUT_DIR, "test.csv")
    train.to_csv(train_path, index=False, encoding="utf-8-sig")
    test.to_csv(test_path, index=False, encoding="utf-8-sig")

    print(f"Da ghi: {train_path} ({len(train)} dong)")
    print(f"Da ghi: {test_path} ({len(test)} dong)")


if __name__ == "__main__":
    main()