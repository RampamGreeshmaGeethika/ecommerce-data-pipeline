import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "data", "raw")
INPUT = os.path.join(RAW, "ecommerce_sales.csv")

def main():
    print("Reading:", INPUT)
    df = pd.read_csv(INPUT)
    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())

    df.to_csv(os.path.join(RAW, "orders_raw.csv"), index=False)
    print("Saved orders_raw.csv")

if __name__ == "__main__":
    main()
