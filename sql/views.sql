CREATE OR REPLACE VIEW gold.vw_monthly_sales AS
SELECT
    order_year,
    order_month,
    order_count,
    units_sold,
    gross_sales,
    avg_order_value
FROM gold.agg_monthly_sales;

CREATE OR REPLACE VIEW gold.vw_top_categories AS
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(quantity) AS total_units
FROM gold.fct_orders
GROUP BY category
ORDER BY total_sales DESC;

CREATE OR REPLACE VIEW gold.vw_state_performance AS
SELECT
    state,
    order_count,
    gross_sales
FROM gold.agg_state_sales
ORDER BY gross_sales DESC;
