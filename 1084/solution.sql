SELECT DISTINCT Product.product_id, Product.product_name 
FROM Product
JOIN Sales ON Sales.product_id = Product.product_id 
WHERE NOT EXISTS (
    SELECT *
    FROM Sales
    WHERE Sales.product_id = Product.product_id 
    AND Sales.sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
)