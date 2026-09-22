import io
import os
import re
import sys

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import pandas as pd
import psycopg2

ROOT = os.path.dirname(os.path.abspath(__file__))

DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "hnv",
    "password": "123456",
}

SCHEMA = "credit_model"

STEP_DIRS = ["step_1", "step_2", "step_3", "step_4"]


def sanitize_identifier(value):
    value = re.sub(r"[^0-9a-zA-Z_]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value.lower()


def sql_ident(value):
    return '"' + value.replace('"', '""') + '"'


def pg_type(series):
    import numpy as np

    if pd.api.types.is_integer_dtype(series):
        return "BIGINT"
    if pd.api.types.is_float_dtype(series):
        return "DOUBLE PRECISION"
    if pd.api.types.is_bool_dtype(series):
        return "BOOLEAN"
    return "TEXT"


def collect_csv_files():
    files = []
    for step in STEP_DIRS:
        step_dir = os.path.join(ROOT, step)
        step_num = step.replace("step_", "")
        for sub in ("input", "output"):
            sub_dir = os.path.join(step_dir, sub)
            if not os.path.isdir(sub_dir):
                continue
            for filename in sorted(os.listdir(sub_dir)):
                if filename.endswith(".csv"):
                    files.append((step_num, sub, os.path.join(sub_dir, filename), filename))
    return files


def table_exists(cur, table):
    cur.execute(
        "SELECT 1 FROM information_schema.tables WHERE table_schema = %s AND table_name = %s",
        (SCHEMA, table),
    )
    return cur.fetchone() is not None


def load_csv_to_db(cur, step, sub, csv_path, filename):
    stem = sanitize_identifier(os.path.splitext(filename)[0])
    table = f"step_{step}_{sub}_{stem}"
    table_ident = sql_ident(table)

    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    cols = list(df.columns)

    cur.execute(f"DROP TABLE IF EXISTS {sql_ident(SCHEMA)}.{table_ident} CASCADE")
    col_defs = ", ".join(f"{sql_ident(c)} {pg_type(df[c])}" for c in cols)
    cur.execute(
        f"CREATE TABLE {sql_ident(SCHEMA)}.{table_ident} ({col_defs})"
    )
    cur.execute(
        f"COMMENT ON TABLE {sql_ident(SCHEMA)}.{table_ident} IS 'source: {os.path.relpath(csv_path, ROOT)}'"
    )

    cleaned = df.where(pd.notnull(df), None)
    buf = io.StringIO()
    cleaned.to_csv(buf, index=False, header=False, na_rep="\\N")
    buf.seek(0)

    copy_sql = (
        f"COPY {sql_ident(SCHEMA)}.{table_ident} "
        f"({', '.join(sql_ident(c) for c in cols)}) FROM STDIN WITH CSV NULL '\\N'"
    )
    cur.copy_expert(copy_sql, buf)
    return len(df)


def main():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = False
    cur = conn.cursor()
    try:
        cur.execute(f"CREATE SCHEMA IF NOT EXISTS {sql_ident(SCHEMA)}")
        conn.commit()

        files = collect_csv_files()
        print(f"Tìm thấy {len(files)} file CSV")

        total_rows = 0
        for step, sub, csv_path, filename in files:
            rows = load_csv_to_db(cur, step, sub, csv_path, filename)
            stem = sanitize_identifier(os.path.splitext(filename)[0])
            table = f"step_{step}_{sub}_{stem}"
            print(f"  {table}: {rows} dòng")
            total_rows += rows
            conn.commit()

        print(f"\nTổng {len(files)} bảng, {total_rows} dòng đã load vào schema {SCHEMA}")
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()