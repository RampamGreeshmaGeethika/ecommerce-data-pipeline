from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = REPO_ROOT / ".env"

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)


@dataclass(frozen=True)
class PipelineConfig:
    env: str
    storage_mode: str
    scale_factor: int
    raw_source_path: str
    output_root: str
    s3_bucket: str
    s3_prefix: str
    aws_region: str
    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

    @property
    def bronze_orders_path(self) -> str:
        return self._dataset_path("bronze/orders")

    @property
    def silver_orders_path(self) -> str:
        return self._dataset_path("silver/orders")

    @property
    def gold_fact_orders_path(self) -> str:
        return self._dataset_path("gold/fct_orders")

    @property
    def gold_dim_products_path(self) -> str:
        return self._dataset_path("gold/dim_products")

    @property
    def gold_daily_sales_path(self) -> str:
        return self._dataset_path("gold/agg_daily_sales")

    @property
    def gold_monthly_sales_path(self) -> str:
        return self._dataset_path("gold/agg_monthly_sales")

    @property
    def gold_state_sales_path(self) -> str:
        return self._dataset_path("gold/agg_state_sales")

    def _dataset_path(self, suffix: str) -> str:
        if self.storage_mode == "s3":
            prefix = self.s3_prefix.strip("/")
            return f"s3a://{self.s3_bucket}/{prefix}/{suffix}" if prefix else f"s3a://{self.s3_bucket}/{suffix}"
        return str(Path(self.output_root) / suffix)


def load_config() -> PipelineConfig:
    storage_mode = os.getenv("PIPELINE_STORAGE_MODE", "local").strip().lower()
    if storage_mode not in {"local", "s3"}:
        raise ValueError("PIPELINE_STORAGE_MODE must be 'local' or 's3'")

    return PipelineConfig(
        env=os.getenv("PIPELINE_ENV", "dev"),
        storage_mode=storage_mode,
        scale_factor=int(os.getenv("PIPELINE_SCALE_FACTOR", "12")),
        raw_source_path=os.getenv("PIPELINE_RAW_SOURCE_PATH", str(REPO_ROOT / "data" / "raw" / "ecommerce_sales.csv")),
        output_root=os.getenv("PIPELINE_OUTPUT_ROOT", str(REPO_ROOT / "data" / "processed")),
        s3_bucket=os.getenv("PIPELINE_S3_BUCKET", ""),
        s3_prefix=os.getenv("PIPELINE_S3_PREFIX", "ecommerce-analytics"),
        aws_region=os.getenv("PIPELINE_AWS_REGION", "us-east-1"),
        postgres_host=os.getenv("PIPELINE_POSTGRES_HOST", "localhost"),
        postgres_port=int(os.getenv("PIPELINE_POSTGRES_PORT", "5432")),
        postgres_db=os.getenv("PIPELINE_POSTGRES_DB", "analytics"),
        postgres_user=os.getenv("PIPELINE_POSTGRES_USER", "postgres"),
        postgres_password=os.getenv("PIPELINE_POSTGRES_PASSWORD", "postgres"),
    )
