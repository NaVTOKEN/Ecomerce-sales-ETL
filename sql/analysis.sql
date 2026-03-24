-- Total Sales
SELECT SUM(total_amount) AS total_sales FROM sales;

-- Top Selling Products
SELECT product_name, SUM(quantity) AS total_qty
FROM sales
GROUP BY product_name
ORDER BY total_qty DESC
LIMIT 5;

-- Region-wise Sales
SELECT region, SUM(total_amount) AS sales
FROM sales
GROUP BY region;

-- Daily Sales
SELECT order_date, SUM(total_amount) AS daily_sales
FROM sales
GROUP BY order_date;

-- Payment Method Analysis
SELECT payment_method, COUNT(*) as total_orders
FROM sales
GROUP BY payment_method;
