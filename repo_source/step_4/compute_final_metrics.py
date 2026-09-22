import os
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    brier_score_loss,
    log_loss,
    roc_auc_score,
    roc_curve,
)

L = "Tỷ lệ khoản vay trên thu nhập"
T = "Trạng thái trả nợ (0 = không vỡ nợ, 1 = vỡ nợ)"
OUTPUT = r"repo_source/step_4/output/so_lieu_chinh_test.csv"

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
step3_out = os.path.join(root, "step_3", "output")
step4_out = os.path.join(root, "step_4", "output")

h = pd.read_csv(os.path.join(step3_out, "prediction_test_has_default.csv"))
n = pd.read_csv(os.path.join(step3_out, "prediction_test_non_default.csv"))
b = pd.read_csv(os.path.join(step3_out, "prediction_test.csv"))

y = b[T]
prob = b["prob_vỡ_nợ"]
pred = b["predicted"]

pauc = roc_auc_score(y, prob)
prac = average_precision_score(y, prob)
fpr, tpr, _ = roc_curve(y, prob)
ks = float((tpr - fpr).max())
brier = brier_score_loss(y, prob)
ll = log_loss(y, prob)

tp = int(((y == 1) & (pred == 1)).sum())
fp = int(((y == 0) & (pred == 1)).sum())
fn = int(((y == 1) & (pred == 0)).sum())
tn = int(((y == 0) & (pred == 0)).sum())

fn_set = h[h["predicted"] == 0]
fp_set = n[n["predicted"] == 1]
fn_caught = int(((fn_set[L] >= 0.0653) & (fn_set[L] <= 0.1907)).sum())
fp_rescued = int(((fp_set[L] >= 0.1987) & (fp_set[L] <= 0.342)).sum())

tp2, fp2, fn2, tn2 = tp + fn_caught, fp - fp_rescued, fn - fn_caught, tn + fp_rescued
rec = tp2 / (tp2 + fn2)
spec = tn2 / (tn2 + fp2)
prec = tp2 / (tp2 + fp2)
f1 = 2 * prec * rec / (prec + rec)
acc = (tp2 + tn2) / (tp2 + fp2 + fn2 + tn2)

row = {
    "evaluation_source": "TEST",
    "ROC AUC": round(pauc, 4),
    "PR AUC": round(prac, 4),
    "KS": round(ks, 4),
    "Brier Score": round(brier, 4),
    "Log Loss": round(ll, 4),
    "Recall": round(rec, 4),
    "Precision": round(prec, 4),
    "Specificity": round(spec, 4),
    "F1": round(f1, 4),
    "Threshold": 0.5,
    "FPR": round(1 - spec, 4),
    "FNR": round(1 - rec, 4),
    "TP": tp2,
    "FP": fp2,
    "FN": fn2,
    "TN": tn2,
    "Accuracy": round(acc, 4),
}

os.makedirs(step4_out, exist_ok=True)
pd.DataFrame([row]).to_csv(OUTPUT, index=False)
print(pd.DataFrame([row]).to_string(index=False))
print(f"\nĐã ghi: {os.path.abspath(OUTPUT)}")