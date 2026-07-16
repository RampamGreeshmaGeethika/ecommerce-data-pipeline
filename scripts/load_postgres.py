import os
import csv
import psycopg2
from config import *

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED = os.path.join(BASE, "data", "processed")
INPUT = os.path.join(PROCESSED, "orders_processed.csv")

def main():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor()

    with open(INPUT, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    sql = """
        INSERT INTO sales (
            order_id, order_date, status, fulfilment, sales_channel,
            ship_service_level, style, sku, category, size, asin,
            courier_status, quantity, currency, price, city, state,
            postal_code, country, promotion_ids, b2b, fulfilled_by,
            sales, year, month, weekday
        )
        VALUES (
            %(order_id)s, %(order_date)s, %(status)s, %(fulfilment)s, %(sales_channel)s,
            %(ship_service_level)s, %(style)s, %(sku)s, %(category)s, %(size)s, %(asin)s,
            %(courier_status)s, %(quantity)s, %(currency)s, %(price)s, %(city)s, %(state)s,
            %(postal_code)s, %(country)s, %(promotion_ids)s, %(b2b)s, %(fulfilled_by)s,
            %(sales)s, %(year)s, %(month)s, %(weekday)s
        );
    """

    for row in rows:
        cur.execute(sql, row)

    conn.commit()
    cur.close()
    conn.close()

    print(f"Inserted {len(rows)} rows.")

if __name__ == "__main__":
    main()
