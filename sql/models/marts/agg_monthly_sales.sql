SELECT
    order_year,
    order_month,
    order_count,
    units_sold,
    gross_sales,
    avg_order_value
FROM gold.agg_monthly_sales
ORDER BY order_year, order_month;
