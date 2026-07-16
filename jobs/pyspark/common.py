from __future__ import annotations

from pyspark.sql import SparkSession

from pipeline.config import PipelineConfig


def build_spark_session(app_name: str, config: PipelineConfig) -> SparkSession:
    builder = (
        SparkSession.builder.appName(app_name)
        .config("spark.sql.session.timeZone", "UTC")
        .config("spark.sql.shuffle.partitions", "8")
        .config("spark.sql.execution.arrow.pyspark.enabled", "true")
    )

    if config.storage_mode == "s3":
        builder = (
            builder.config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
            .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
            .config("spark.hadoop.fs.s3a.endpoint.region", config.aws_region)
        )

    return builder.getOrCreate()
