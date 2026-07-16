import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "data", "raw")
INPUT = os.path.join(RAW, "ecommerce_sales.csv")
OUTPUT = os.path.join(RAW, "orders_raw.csv")
SCALE_FACTOR = 12

def main():
    print("Reading:", INPUT)
    df = pd.read_csv(INPUT, encoding="utf-8-sig", low_memory=False)
    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())
    print("Projected 1.5M+ workload:", len(df) * SCALE_FACTOR)

    df.to_csv(OUTPUT, index=False)
    print("Saved:", OUTPUT)

if __name__ == "__main__":
    main()
