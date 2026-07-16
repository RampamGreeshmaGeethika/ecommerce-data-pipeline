import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "data", "raw")
PROCESSED = os.path.join(BASE, "data", "processed")

INPUT = os.path.join(RAW, "orders_raw.csv")
OUTPUT = os.path.join(PROCESSED, "orders_processed.csv")

def main():
    df = pd.read_csv(INPUT, encoding="utf-8-sig", low_memory=False)

    df = df.rename(columns={
        "Order ID": "order_id",
        "Date": "order_date",
        "Status": "status",
        "Fulfilment": "fulfilment",
        "Sales Channel ": "sales_channel",
        "ship-service-level": "ship_service_level",
        "Style": "style",
        "SKU": "sku",
        "Category": "category",
        "Size": "size",
        "ASIN": "asin",
        "Courier Status": "courier_status",
        "Qty": "quantity",
        "currency": "currency",
        "Amount": "price",
        "ship-city": "city",
        "ship-state": "state",
        "ship-postal-code": "postal_code",
        "ship-country": "country",
        "promotion-ids": "promotion_ids",
        "B2B": "b2b",
        "fulfilled-by": "fulfilled_by"
    })

    df = df.drop_duplicates()

    df["quantity"] = df["quantity"].fillna(0)
    df["price"] = df["price"].fillna(0)

    df["order_date"] = pd.to_datetime(df["order_date"], format="%m-%d-%y", errors="coerce")
    df = df.dropna(subset=["order_date"])

    df = df[(df["price"] >= 0) & (df["quantity"] >= 0)]

    df["sales"] = df["price"] * df["quantity"]

    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month
    df["weekday"] = df["order_date"].dt.day_name()

    os.makedirs(PROCESSED, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print("Saved:", OUTPUT)
    print("Processed rows:", len(df))

if __name__ == "__main__":
    main()
