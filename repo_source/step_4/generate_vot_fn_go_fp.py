import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(HERE, "input")
IMAGE_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "image"))

matplotlib.rcParams["font.family"] = "Segoe UI"
matplotlib.rcParams["axes.unicode_minus"] = False

PURPLE = "#9A7BD0"
DARK = "#4B2E83"
GRAY = "#706A7C"
LIGHT = "#D6CEE8"
BOX_BG = "#F3EFFB"
BOX_EDGE = "#9A7BD0"

LTI_COL = "Tỷ lệ khoản vay trên thu nhập"

FN_LO, FN_HI = 0.0653, 0.1907
FP_LO, FP_HI = 0.1987, 0.3420


def col_chart(path, title, cond_label, cond_text, caught_label, caught, rest_label, rest, color):
    fig = plt.figure(figsize=(8.5, 6.8), dpi=160)
    gs = fig.add_gridspec(2, 1, height_ratios=[0.42, 1.0], hspace=0.28)

    ax_cond = fig.add_subplot(gs[0])
    ax_cond.axis("off")
    ax_cond.set_xlim(0, 1)
    ax_cond.set_ylim(0, 1)
    box = ax_cond.text(0.5, 0.5,
                       f"{cond_label}:\n{cond_text}",
                       ha="center", va="center", fontsize=12.5, color=DARK,
                       multialignment="center",
                       bbox=dict(boxstyle="round,pad=0.65", facecolor=BOX_BG, edgecolor=BOX_EDGE, linewidth=1.8))

    ax = fig.add_subplot(gs[1])
    labels = [caught_label, rest_label]
    values = [caught, rest]
    colors = [color, LIGHT]
    total = caught + rest

    bars = ax.bar(labels, values, width=0.45, color=colors, edgecolor="white", linewidth=1.2, zorder=3)
    for b, v in zip(bars, values):
        pct = v / total * 100
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:,} — {pct:.1f}%",
                ha="center", va="bottom", fontsize=14, fontweight="bold", color=DARK)
        if v == caught:
            ax.text(b.get_x() + b.get_width() / 2, v / 2, "đúng",
                    ha="center", va="center", fontsize=12, fontweight="bold", color="#ffffff")

    ax.set_ylim(0, max(values) * 1.18)
    ax.set_xlabel("", fontsize=11, color=GRAY)
    ax.set_ylabel("Số khách hàng", fontsize=11, color=GRAY)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color="#E9E5F1", linestyle="--", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", labelsize=12, colors="#000000")

    fig.suptitle(title, fontsize=17, fontweight="bold", color="#000000", y=0.98)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def main():
    os.makedirs(IMAGE_DIR, exist_ok=True)
    h = pd.read_csv(os.path.join(INPUT_DIR, "prediction_test_has_default.csv"))
    n = pd.read_csv(os.path.join(INPUT_DIR, "prediction_test_non_default.csv"))
    fn = h[h["predicted"] == 0]
    fp = n[n["predicted"] == 1]

    fn_caught = ((fn[LTI_COL] >= FN_LO) & (fn[LTI_COL] <= FN_HI)).sum()
    fn_rest = len(fn) - fn_caught
    col_chart(
        path=os.path.join(IMAGE_DIR, "step_4_vot_fn.png"),
        title="BỘ LỌC VỚT FN",
        cond_label="Điều kiện bắt",
        cond_text=f"LTI trong khoảng [{FN_LO:.4f} ; {FN_HI:.4f}] → FN chuyển thành TP",
        caught_label="Bắt được",
        caught=fn_caught,
        rest_label="Còn lại",
        rest=fn_rest,
        color=PURPLE,
    )

    fp_caught = ((fp[LTI_COL] >= FP_LO) & (fp[LTI_COL] <= FP_HI)).sum()
    fp_rest = len(fp) - fp_caught
    col_chart(
        path=os.path.join(IMAGE_DIR, "step_4_go_fp.png"),
        title="BỘ LỌC GỠ FP",
        cond_label="Điều kiện gỡ",
        cond_text=f"LTI trong khoảng [{FP_LO:.4f} ; {FP_HI:.4f}] → FP chuyển về TN",
        caught_label="Gỡ được",
        caught=fp_caught,
        rest_label="Còn lại",
        rest=fp_rest,
        color=PURPLE,
    )

    print(f"FN: bắt {fn_caught:,} ({fn_caught/len(fn)*100:.1f}%), còn {fn_rest:,} ({fn_rest/len(fn)*100:.1f}%)")
    print(f"FP: gỡ {fp_caught:,} ({fp_caught/len(fp)*100:.1f}%), còn {fp_rest:,} ({fp_rest/len(fp)*100:.1f}%)")
    print("Đã tạo 2 ảnh trong", IMAGE_DIR)


if __name__ == "__main__":
    main()