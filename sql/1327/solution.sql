-- Write your PostgreSQL query statement below
SELECT p.product_name, SUM(o.unit) as unit
FROM Products p 
LEFT JOIN Orders o ON (o.order_date BETWEEN '2020-02-01' AND '2020-02-29') AND o.product_id = p.product_id
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100