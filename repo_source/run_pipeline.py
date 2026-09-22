import os
import shutil
import subprocess
import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.abspath(__file__))


def run_step(step_name, script="run.py"):
    step_dir = os.path.join(ROOT, step_name)
    script_path = os.path.join(step_dir, script)
    print(f"\n{'='*60}")
    print(f"  CHẠY {step_name.upper()}")
    print(f"{'='*60}\n")
    child_env = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
    result = subprocess.run([sys.executable, script_path], cwd=step_dir, env=child_env)
    if result.returncode != 0:
        print(f"\n[LOI] {step_name} that bai (exit code {result.returncode})")
        sys.exit(result.returncode)


def run_main_pipeline():
    print("\n" + "#" * 60)
    print("  KHỞI CHẠY LUỒNG CHÍNH (PRODUCTION PIPELINE): BƯỚC 1 -> BƯỚC 2 -> BƯỚC 3 -> BƯỚC 4")
    print("#" * 60)

    # step_1: excel -> train.csv + test.csv
    run_step("step_1")

    # step_2: train.csv -> model baseline (8 bien tho)
    os.makedirs(os.path.join(ROOT, "step_2", "input"), exist_ok=True)
    shutil.copy2(os.path.join(ROOT, "step_1", "output", "train.csv"),
                 os.path.join(ROOT, "step_2", "input", "train.csv"))
    run_step("step_2")

    # step_3: model baseline + train/test -> prediction baseline (split theo target)
    os.makedirs(os.path.join(ROOT, "step_3", "input"), exist_ok=True)
    shutil.copy2(os.path.join(ROOT, "step_2", "output", "model.pkl"),
                 os.path.join(ROOT, "step_3", "input", "model.pkl"))
    shutil.copy2(os.path.join(ROOT, "step_2", "output", "metadata.json"),
                 os.path.join(ROOT, "step_3", "input", "metadata.json"))
    scaler_src = os.path.join(ROOT, "step_2", "output", "scaler.pkl")
    if os.path.exists(scaler_src):
        shutil.copy2(scaler_src, os.path.join(ROOT, "step_3", "input", "scaler.pkl"))
    shutil.copy2(os.path.join(ROOT, "step_1", "output", "test.csv"),
                 os.path.join(ROOT, "step_3", "input", "test.csv"))
    shutil.copy2(os.path.join(ROOT, "step_1", "output", "train.csv"),
                 os.path.join(ROOT, "step_3", "input", "train.csv"))
    run_step("step_3")

    # step_4: Risk Adjustment (Lớp GỠ/VỚT) áp trên nền dự đoán baseline của Bước 3
    #         + test.csv từ Bước 1 để tự dựng 4 biến tương tác nghiệp vụ
    os.makedirs(os.path.join(ROOT, "step_4", "input"), exist_ok=True)
    for f in ("prediction_test_has_default.csv", "prediction_test_non_default.csv"):
        src = os.path.join(ROOT, "step_3", "output", f)
        dst = os.path.join(ROOT, "step_4", "input", f)
        shutil.copy2(src, dst)
    shutil.copy2(os.path.join(ROOT, "step_1", "output", "test.csv"),
                 os.path.join(ROOT, "step_4", "input", "test.csv"))
    run_step("step_4")

    print(f"\n{'='*60}")
    print("  HOÀN THÀNH LUỒNG CHÍNH (BƯỚC 1 -> BƯỚC 2 -> BƯỚC 3 -> BƯỚC 4)")
    print(f"{'='*60}")
    for step in ["step_1", "step_2", "step_3", "step_4"]:
        output_dir = os.path.join(ROOT, step, "output")
        files = [f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))]
        print(f"  {step}/output/: {files}")


def run_benchmark_pipeline():
    print("\n" + "#" * 60)
    print("  CHẠY RIÊNG BƯỚC 2 -> BƯỚC 3 (tập con của luồng chính)")
    print("#" * 60)

    # step_2: train.csv -> model baseline (chưa chuẩn hóa)
    os.makedirs(os.path.join(ROOT, "step_2", "input"), exist_ok=True)
    shutil.copy2(os.path.join(ROOT, "step_1", "output", "train.csv"),
                 os.path.join(ROOT, "step_2", "input", "train.csv"))
    run_step("step_2")

    # step_3: model baseline + test -> prediction baseline
    os.makedirs(os.path.join(ROOT, "step_3", "input"), exist_ok=True)
    shutil.copy2(os.path.join(ROOT, "step_2", "output", "model.pkl"),
                 os.path.join(ROOT, "step_3", "input", "model.pkl"))
    shutil.copy2(os.path.join(ROOT, "step_2", "output", "metadata.json"),
                 os.path.join(ROOT, "step_3", "input", "metadata.json"))
    scaler_src = os.path.join(ROOT, "step_2", "output", "scaler.pkl")
    if os.path.exists(scaler_src):
        shutil.copy2(scaler_src, os.path.join(ROOT, "step_3", "input", "scaler.pkl"))
    shutil.copy2(os.path.join(ROOT, "step_1", "output", "test.csv"),
                 os.path.join(ROOT, "step_3", "input", "test.csv"))
    shutil.copy2(os.path.join(ROOT, "step_1", "output", "train.csv"),
                 os.path.join(ROOT, "step_3", "input", "train.csv"))
    run_step("step_3")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Credit Scoring Pipeline Coordinator")
    parser.add_argument("--all", action="store_true", help="Bí danh của luồng chính 1->2->3->4 (giữ tương thích)")
    parser.add_argument("--benchmark-only", action="store_true", help="Chỉ chạy riêng bước 2, 3")
    args = parser.parse_args()

    if args.benchmark_only:
        run_benchmark_pipeline()
    elif args.all:
        run_main_pipeline()
        print(f"\n{'='*60}")
        print("  HOÀN THÀNH TOÀN BỘ PIPELINE (LUỒNG CHÍNH 1->2->3->4)")
        print(f"{'='*60}")
    else:
        run_main_pipeline()
        print("\n[GHI CHÚ] Mặc định hệ thống chạy LUỒNG CHÍNH (Bước 1 -> Bước 2 -> Bước 3 -> Bước 4).")


if __name__ == "__main__":
    main()
