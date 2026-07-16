from __future__ import annotations

from pyspark.sql import functions as F

from jobs.pyspark.common import build_spark_session
from pipeline.config import load_config


def main() -> None:
    config = load_config()
    spark = build_spark_session("ecommerce_gold_analytics", config)

    silver_df = spark.read.parquet(config.silver_orders_path)

    fact_orders = silver_df.select(
        "order_id",
        "order_date",
        "order_year",
        "order_month",
        "order_day",
        "order_weekday",
        "status",
        "is_cancelled",
        "fulfilment",
        "sales_channel",
        "ship_service_level",
        "style",
        "sku",
        "category",
        "size",
        "asin",
        "courier_status",
        "quantity",
        "currency",
        "price",
        "sales",
        "city",
        "state",
        "postal_code",
        "country",
        "promotion_ids",
        "b2b",
        "fulfilled_by",
    )

    dim_products = (
        silver_df.select("sku", "asin", "style", "category", "size")
        .dropna(subset=["sku"])
        .dropDuplicates(["sku"])
    )

    daily_sales = (
        silver_df.groupBy("order_date", "order_year", "order_month")
        .agg(
            F.count("*").alias("order_count"),
            F.sum("quantity").alias("units_sold"),
            F.sum("sales").alias("gross_sales"),
            F.sum(F.when(~F.col("is_cancelled"), F.col("sales")).otherwise(F.lit(0))).alias("net_sales"),
        )
        .orderBy("order_date")
    )

    monthly_sales = (
        silver_df.groupBy("order_year", "order_month")
        .agg(
            F.count("*").alias("order_count"),
            F.sum("quantity").alias("units_sold"),
            F.sum("sales").alias("gross_sales"),
            F.avg("sales").alias("avg_order_value"),
        )
        .orderBy("order_year", "order_month")
    )

    state_sales = (
        silver_df.groupBy("state")
        .agg(
            F.count("*").alias("order_count"),
            F.sum("sales").alias("gross_sales"),
        )
        .orderBy(F.desc("gross_sales"))
    )

    fact_orders.write.mode("overwrite").parquet(config.gold_fact_orders_path)
    dim_products.write.mode("overwrite").parquet(config.gold_dim_products_path)
    daily_sales.write.mode("overwrite").parquet(config.gold_daily_sales_path)
    monthly_sales.write.mode("overwrite").parquet(config.gold_monthly_sales_path)
    state_sales.write.mode("overwrite").parquet(config.gold_state_sales_path)

    print(f"Gold datasets written under {config._dataset_path('gold')}")
    spark.stop()


if __name__ == "__main__":
    main()
