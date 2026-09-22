import glob
import json
import os

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    roc_auc_score,
)

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(HERE, "input")
OUTPUT_DIR = os.path.join(HERE, "output")

TARGET_COLUMN = "Trạng thái trả nợ (0 = không vỡ nợ, 1 = vỡ nợ)"
ID_COLUMNS = ["Mã khách hàng"]

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


def read_train_csv(input_dir):
    csv_files = [f for f in glob.glob(os.path.join(input_dir, "*.csv")) if "final" not in os.path.basename(f)]
    if not csv_files:
        raise FileNotFoundError(f"Không tìm thấy file csv trong {input_dir}")
    return pd.read_csv(csv_files[0])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Đọc dữ liệu train từ {INPUT_DIR}...")
    df = read_train_csv(INPUT_DIR)
    print(f"Tổng số dòng: {len(df)}, cột: {list(df.columns)}")

    target = TARGET_COLUMN if TARGET_COLUMN else df.columns[-1]
    if FEATURE_COLUMNS:
        feature_cols = [c for c in FEATURE_COLUMNS if c in df.columns]
    else:
        feature_cols = [c for c in df.columns if c != target]

    missing = [c for c in FEATURE_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Thiếu cột trong train.csv: {missing}")

    id_cols = [c for c in ID_COLUMNS if c in df.columns]
    print(f"ID columns: {id_cols}")

    train_final = df[feature_cols + [target]].copy()
    train_final_path = os.path.join(OUTPUT_DIR, "train_final.csv")
    train_final.to_csv(train_final_path, index=False, encoding="utf-8-sig")
    print(f"Bước 1 — Sinh train_final.csv: {train_final_path} ({len(train_final)} dòng, {len(feature_cols)} features)")

    X = train_final[feature_cols]
    y = train_final[target]

    print(f"Feature ({len(feature_cols)}): {feature_cols}")
    print(f"Target: {target}")

    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X, y)

    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)[:, 1]

    metrics = {
        "accuracy": float(accuracy_score(y, y_pred)),
        "auc": float(roc_auc_score(y, y_prob)),
    }
    print(f"Bước 2 — Huấn luyện xong. Accuracy: {metrics['accuracy']:.4f}, AUC: {metrics['auc']:.4f}")

    print(f"\nBáo cáo phân loại (train):")
    print(classification_report(y, y_pred, target_names=["Không vỡ nợ", "Vỡ nợ"]))

    model_path = os.path.join(OUTPUT_DIR, "model.pkl")
    metadata_path = os.path.join(OUTPUT_DIR, "metadata.json")
    joblib.dump(model, model_path)

    metadata = {
        "model_type": "LogisticRegression",
        "model_path": model_path,
        "train_final_path": train_final_path,
        "feature_columns": feature_cols,
        "target_column": target,
        "id_columns": id_cols,
        "n_samples": int(len(train_final)),
        "metrics": metrics,
    }
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"Đã lưu model: {model_path}")
    print(f"Đã lưu metadata: {metadata_path}")


if __name__ == "__main__":
    main()