from __future__ import annotations

from pyspark.sql import functions as F

from jobs.pyspark.common import build_spark_session
from pipeline.config import load_config


def main() -> None:
    config = load_config()
    spark = build_spark_session("ecommerce_bronze_ingestion", config)

    source_df = (
        spark.read.option("header", True)
        .option("mode", "FAILFAST")
        .csv(config.raw_source_path)
        .withColumn("source_row_id", F.monotonically_increasing_id())
    )

    multiplier_df = spark.range(0, config.scale_factor).withColumnRenamed("id", "batch_id")

    bronze_df = (
        source_df.crossJoin(multiplier_df)
        .withColumn("source_file", F.lit(config.raw_source_path))
        .withColumn("ingested_at", F.current_timestamp())
        .withColumn("scale_batch", F.col("batch_id"))
        .withColumn(
            "synthetic_order_id",
            F.concat_ws("-", F.col("Order ID"), F.lpad(F.col("batch_id").cast("string"), 2, "0")),
        )
    )

    (
        bronze_df.write.mode("overwrite")
        .partitionBy("scale_batch")
        .parquet(config.bronze_orders_path)
    )

    record_count = bronze_df.count()
    print(f"Bronze load complete: {record_count} rows written to {config.bronze_orders_path}")
    spark.stop()


if __name__ == "__main__":
    main()
