CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;

CREATE TABLE IF NOT EXISTS gold.fct_orders (
    order_id TEXT PRIMARY KEY,
    order_date DATE,
    order_year INTEGER,
    order_month INTEGER,
    order_day INTEGER,
    order_weekday TEXT,
    status TEXT,
    is_cancelled BOOLEAN,
    fulfilment TEXT,
    sales_channel TEXT,
    ship_service_level TEXT,
    style TEXT,
    sku TEXT,
    category TEXT,
    size TEXT,
    asin TEXT,
    courier_status TEXT,
    quantity INTEGER,
    currency TEXT,
    price NUMERIC(18, 2),
    sales NUMERIC(18, 2),
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT,
    promotion_ids TEXT,
    b2b BOOLEAN,
    fulfilled_by TEXT
);

CREATE TABLE IF NOT EXISTS gold.dim_products (
    sku TEXT PRIMARY KEY,
    asin TEXT,
    style TEXT,
    category TEXT,
    size TEXT
);

CREATE TABLE IF NOT EXISTS gold.agg_daily_sales (
    order_date DATE,
    order_year INTEGER,
    order_month INTEGER,
    order_count BIGINT,
    units_sold BIGINT,
    gross_sales NUMERIC(18, 2),
    net_sales NUMERIC(18, 2)
);

CREATE TABLE IF NOT EXISTS gold.agg_monthly_sales (
    order_year INTEGER,
    order_month INTEGER,
    order_count BIGINT,
    units_sold BIGINT,
    gross_sales NUMERIC(18, 2),
    avg_order_value NUMERIC(18, 2)
);

CREATE TABLE IF NOT EXISTS gold.agg_state_sales (
    state TEXT,
    order_count BIGINT,
    gross_sales NUMERIC(18, 2)
);
