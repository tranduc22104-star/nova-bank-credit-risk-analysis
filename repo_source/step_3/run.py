import glob
import json
import os

import joblib
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(HERE, "input")
OUTPUT_DIR = os.path.join(HERE, "output")


def find_file(input_dir, name):
    path = os.path.join(input_dir, name)
    if os.path.exists(path):
        return path
    matches = glob.glob(os.path.join(input_dir, f"*{name}*"))
    return matches[0] if matches else None


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    model_path = find_file(input_dir=INPUT_DIR, name="model.pkl")
    metadata_path = find_file(input_dir=INPUT_DIR, name="metadata.json")

    if not model_path:
        raise FileNotFoundError(f"Không tìm thấy model.pkl trong {INPUT_DIR}")
    if not metadata_path:
        raise FileNotFoundError(f"Không tìm thấy metadata.json trong {INPUT_DIR}")

    model = joblib.load(model_path)
    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    feature_cols = metadata["feature_columns"]
    target = metadata["target_column"]
    id_cols = [c for c in metadata.get("id_columns", [])]
    has_proba = hasattr(model, "predict_proba")

    csv_files = [f for f in glob.glob(os.path.join(INPUT_DIR, "*.csv")) if "final" not in os.path.basename(f)]
    if not csv_files:
        raise FileNotFoundError(f"Không tìm thấy file csv trong {INPUT_DIR}")

    for csv_path in csv_files:
        fname = os.path.basename(csv_path)
        name = os.path.splitext(fname)[0]
        df = pd.read_csv(csv_path)
        missing = [c for c in feature_cols + [target] if c not in df.columns]
        if missing:
            print(f"Bỏ qua {name}: thiếu cột {missing}")
            continue

        carry_cols = [c for c in id_cols + feature_cols if c in df.columns] + [target]

        final_df = df[carry_cols].copy()
        final_path = os.path.join(OUTPUT_DIR, f"{name}_final.csv")
        final_df.to_csv(final_path, index=False, encoding="utf-8-sig")
        print(f"Bước 1 — Sinh {name}_final.csv: {final_path} ({len(final_df)} dòng)")

        X = final_df[feature_cols]
        y = final_df[target]
        y_pred = model.predict(X)

        result = final_df.copy()
        result["predicted"] = y_pred
        if has_proba:
            result["prob_vỡ_nợ"] = model.predict_proba(X)[:, 1]
        if y_pred.dtype == y.dtype:
            result["correct"] = (y_pred == y).astype(int)

        out_path = os.path.join(OUTPUT_DIR, f"prediction_{name}.csv")
        result.to_csv(out_path, index=False, encoding="utf-8-sig")
        print(f"Bước 2 — Đã ghi: {out_path} ({len(result)} dòng)")

        acc = result["correct"].mean() * 100 if "correct" in result.columns else None
        if acc is not None:
            print(f"  Accuracy: {acc:.2f}%")

        non_def = result[result[target] == 0].copy()
        has_def = result[result[target] == 1].copy()
        non_path = os.path.join(OUTPUT_DIR, f"prediction_{name}_non_default.csv")
        has_path = os.path.join(OUTPUT_DIR, f"prediction_{name}_has_default.csv")
        non_def.to_csv(non_path, index=False, encoding="utf-8-sig")
        has_def.to_csv(has_path, index=False, encoding="utf-8-sig")
        print(f"Bước 3 — Tách theo target:")
        print(f"  -> {non_path} ({len(non_def)} dòng, target=0)")
        print(f"  -> {has_path} ({len(has_def)} dòng, target=1)")


if __name__ == "__main__":
    main()