CREATE VIEW monthly_sales AS
SELECT year, month, SUM(sales) AS total_sales
FROM sales
GROUP BY year, month;

CREATE VIEW top_categories AS
SELECT category, SUM(sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;
