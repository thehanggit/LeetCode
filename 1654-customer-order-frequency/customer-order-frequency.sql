-- with cte as (
--     select
--         o.customer_id,
--         o.product_id,
--         o.quantity,
--         o.order_date,
--         p.price
--     from
--         Orders o
--     left join
--         Product p
--     on
--         o.product_id = p.product_id
-- ),

-- june as (
--     select
--         customer_id
--     from
--         cte
--     where
--         year(order_date) = 2020
--         and month(order_date) = 6
--     group by
--         customer_id
--     having
--         sum(quantity * price) >= 100
-- ),

-- july as (
--     select
--         customer_id
--     from
--         cte
--     where
--         year(order_date) = 2020
--         and month(order_date) = 7
--     group by
--         customer_id
--     having
--         sum(quantity * price) >= 100   
-- )

-- select
--     c.customer_id,
--     c.name
-- from
--     Customers c
-- inner join
--     june
-- on
--     c.customer_id = june.customer_id
-- inner join
--     july
-- on
--     june.customer_id = july.customer_id



select
    customer_id,
    name
from
    Customers 
join
    Orders using (customer_id)
join
    Product using (product_id)
where
    year(order_date) = 2020
group by
    customer_id
having
    sum(
        if(month(order_date) = 6, quantity, 0) * price
    ) >= 100
    and
    sum(
        if(month(order_date) = 7, quantity, 0) * price
    ) >= 100