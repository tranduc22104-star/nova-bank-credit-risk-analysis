import json
import os

import joblib
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(HERE, "output", "model.pkl")
METADATA_PATH = os.path.join(HERE, "output", "metadata.json")
OUTPUT_PATH = os.path.join(HERE, "output", "trong_so_model.csv")

model = joblib.load(MODEL_PATH)
metadata = json.load(open(METADATA_PATH, encoding="utf-8"))

feature_cols = metadata["feature_columns"]
coef = model.coef_[0]
intercept = float(model.intercept_[0])

rows = [
    {"Biến": c, "trọng số (coef)": w}
    for c, w in zip(feature_cols, coef)
]
rows.append({"Biến": "Intercept (hằng số)", "trọng số (coef)": intercept})

df = pd.DataFrame(rows, columns=["Biến", "trọng số (coef)"])
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

print(df.to_string(index=False))
print("Đã ghi:", os.path.abspath(OUTPUT_PATH))