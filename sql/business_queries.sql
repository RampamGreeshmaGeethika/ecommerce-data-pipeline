-- Monthly revenue trend
SELECT
    order_year,
    order_month,
    gross_sales,
    avg_order_value
FROM gold.agg_monthly_sales
ORDER BY order_year, order_month;

-- Top performing categories
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(quantity) AS units_sold
FROM gold.fct_orders
GROUP BY category
ORDER BY total_sales DESC
LIMIT 10;

-- Highest revenue states
SELECT
    state,
    gross_sales,
    order_count
FROM gold.agg_state_sales
ORDER BY gross_sales DESC
LIMIT 10;

-- Cancelled order share
SELECT
    is_cancelled,
    COUNT(*) AS order_count,
    SUM(sales) AS revenue
FROM gold.fct_orders
GROUP BY is_cancelled;

-- Best selling SKUs
SELECT
    sku,
    style,
    category,
    SUM(quantity) AS units_sold,
    SUM(sales) AS total_sales
FROM gold.fct_orders
GROUP BY sku, style, category
ORDER BY total_sales DESC
LIMIT 20;
