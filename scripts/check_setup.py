from __future__ import annotations

import csv
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = REPO_ROOT / ".env"
RAW_DIR = REPO_ROOT / "data" / "raw"
DATASET_PATH = RAW_DIR / "ecommerce_sales.csv"


def count_rows(csv_path: Path) -> int:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        return max(sum(1 for _ in handle) - 1, 0)


def main() -> int:
    errors: list[str] = []

    print("Checking local project setup...\n")

    if ENV_FILE.exists():
        print(f"[OK] Environment file found: {ENV_FILE}")
    else:
        errors.append(
            "Missing .env file. Create it by copying .env.example:\n"
            "  Copy-Item .env.example .env"
        )

    if DATASET_PATH.exists():
        row_count = count_rows(DATASET_PATH)
        print(f"[OK] Dataset found: {DATASET_PATH}")
        print(f"[OK] Dataset rows detected: {row_count:,}")
    else:
        errors.append(
            "Missing source dataset.\n"
            "Download the Amazon Sale Report / e-commerce sales CSV from Kaggle,\n"
            f"then place it here:\n  {DATASET_PATH}\n"
            "If the downloaded file has a different name, rename it to:\n"
            "  ecommerce_sales.csv"
        )

    if errors:
        print("\nSetup check failed:\n")
        for index, error in enumerate(errors, start=1):
            print(f"{index}. {error}\n")
        return 1

    print("\nSetup check passed. You can start the project with:")
    print("  docker compose up airflow-init")
    print("  docker compose up -d")
    print("  docker compose exec airflow-webserver airflow dags trigger ecommerce_analytics_pipeline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
