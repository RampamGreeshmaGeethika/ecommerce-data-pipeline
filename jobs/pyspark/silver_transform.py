from __future__ import annotations

from pyspark.sql import functions as F
from pyspark.sql.types import DecimalType, IntegerType

from jobs.pyspark.common import build_spark_session
from pipeline.config import load_config


def main() -> None:
    config = load_config()
    spark = build_spark_session("ecommerce_silver_transform", config)

    bronze_df = spark.read.parquet(config.bronze_orders_path)

    silver_df = (
        bronze_df.select(
            F.col("synthetic_order_id").alias("order_id"),
            F.col("Date").alias("order_date_raw"),
            F.col("Status").alias("status"),
            F.col("Fulfilment").alias("fulfilment"),
            F.trim(F.col("Sales Channel ")).alias("sales_channel"),
            F.col("ship-service-level").alias("ship_service_level"),
            F.col("Style").alias("style"),
            F.col("SKU").alias("sku"),
            F.col("Category").alias("category"),
            F.col("Size").alias("size"),
            F.col("ASIN").alias("asin"),
            F.col("Courier Status").alias("courier_status"),
            F.col("Qty").cast(IntegerType()).alias("quantity"),
            F.col("currency").alias("currency"),
            F.regexp_replace(F.col("Amount"), ",", "").cast(DecimalType(18, 2)).alias("price"),
            F.initcap(F.trim(F.col("ship-city"))).alias("city"),
            F.upper(F.trim(F.col("ship-state"))).alias("state"),
            F.regexp_replace(F.col("ship-postal-code").cast("string"), "\\.0$", "").alias("postal_code"),
            F.upper(F.trim(F.col("ship-country"))).alias("country"),
            F.col("promotion-ids").alias("promotion_ids"),
            F.col("B2B").cast("boolean").alias("b2b"),
            F.col("fulfilled-by").alias("fulfilled_by"),
            F.col("scale_batch"),
            F.col("source_row_id"),
            F.col("source_file"),
            F.col("ingested_at"),
        )
        .withColumn("order_date", F.to_date("order_date_raw", "MM-dd-yy"))
        .drop("order_date_raw")
        .dropDuplicates(["order_id"])
        .fillna({"quantity": 0})
        .fillna({"price": 0})
        .filter(F.col("order_date").isNotNull())
        .filter(F.col("quantity") >= 0)
        .filter(F.col("price") >= 0)
        .withColumn("sales", (F.col("price") * F.col("quantity")).cast(DecimalType(18, 2)))
        .withColumn("order_year", F.year("order_date"))
        .withColumn("order_month", F.month("order_date"))
        .withColumn("order_day", F.dayofmonth("order_date"))
        .withColumn("order_weekday", F.date_format("order_date", "EEEE"))
        .withColumn("is_cancelled", F.lower(F.col("status")) == F.lit("cancelled"))
    )

    silver_df.write.mode("overwrite").partitionBy("order_year", "order_month").parquet(config.silver_orders_path)

    record_count = silver_df.count()
    print(f"Silver transform complete: {record_count} rows written to {config.silver_orders_path}")
    spark.stop()


if __name__ == "__main__":
    main()
