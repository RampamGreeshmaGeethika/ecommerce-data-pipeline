-- Top categories
SELECT category, SUM(sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- Monthly revenue
SELECT year, month, SUM(sales) AS revenue
FROM sales
GROUP BY year, month
ORDER BY year, month;

-- Top cities
SELECT city, SUM(sales) AS total_sales
FROM sales
GROUP BY city
ORDER BY total_sales DESC;

-- Fulfilment Type Breakdown
SELECT fulfilment, SUM(sales) AS total_sales
FROM sales
GROUP BY fulfilment
ORDER BY total_sales DESC;

-- Sales Channel Performance
SELECT sales_channel, SUM(sales) AS total_sales
FROM sales
GROUP BY sales_channel
ORDER BY total_sales DESC;

-- B2B vs B2C
SELECT b2b, SUM(sales) AS total_sales
FROM sales
GROUP BY b2b;

-- Courier Status Breakdown
SELECT courier_status, COUNT(*) AS orders
FROM sales
GROUP BY courier_status;

-- Top SKUs
SELECT sku, SUM(sales) AS total_sales
FROM sales
GROUP BY sku
ORDER BY total_sales DESC
LIMIT 20;

-- Top Styles (product names)
SELECT style, SUM(sales) AS total_sales
FROM sales
GROUP BY style
ORDER BY total_sales DESC
LIMIT 20;

-- Country Breakdown
SELECT country, SUM(sales) AS total_sales
FROM sales
GROUP BY country
ORDER BY total_sales DESC;

