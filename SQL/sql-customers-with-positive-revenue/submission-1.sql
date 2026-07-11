-- Write your query below
WITH base_cte AS (
SELECT
    SUM(revenue) as rev,
    customer_id
FROM customers
WHERE 1=1
AND year = 2020
GROUP BY customer_id
)

SELECT customer_id FROM base_cte
WHERE 1=1
AND rev > 0