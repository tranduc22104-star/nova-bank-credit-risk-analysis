import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(HERE, "input")
OUTPUT_DIR = os.path.join(HERE, "output")

LTI_COL = "Tỷ lệ khoản vay trên thu nhập"

FN_LO, FN_HI = 0.0653, 0.1907
FP_LO, FP_HI = 0.1987, 0.3420


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    h = pd.read_csv(os.path.join(INPUT_DIR, "prediction_test_has_default.csv"))
    n = pd.read_csv(os.path.join(INPUT_DIR, "prediction_test_non_default.csv"))

    fn_left = h[(h["predicted"] == 0) & ~h[LTI_COL].between(FN_LO, FN_HI)]
    fp_left = n[(n["predicted"] == 1) & ~n[LTI_COL].between(FP_LO, FP_HI)]

    fn_path = os.path.join(OUTPUT_DIR, "con_lai_fn_sau_cat.csv")
    fp_path = os.path.join(OUTPUT_DIR, "con_lai_fp_sau_cat.csv")
    fn_left.to_csv(fn_path, index=False, encoding="utf-8-sig")
    fp_left.to_csv(fp_path, index=False, encoding="utf-8-sig")

    print(f"FN còn sót lại: {len(fn_left)}/{int((h['predicted'] == 0).sum())} -> {fn_path}")
    print(f"FP còn sót lại: {len(fp_left)}/{int((n['predicted'] == 1).sum())} -> {fp_path}")


if __name__ == "__main__":
    main()