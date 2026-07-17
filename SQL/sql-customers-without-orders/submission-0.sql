-- Write your query below
select name from customers c
where true
and c.id not in (select customer_id from orders)