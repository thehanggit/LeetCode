-- with june as (
--     select
--         customer_id
--     from
--         Orders o
--     join
--         Product p
--     on
--         o.product_id = p.product_id
--     where
--         date_format(order_date, '%Y-%m') = '2020-06'
--     group by
--         customer_id
--     having
--         sum(o.quantity * p.price) >= 100
-- ),

-- july as (
--     select
--         customer_id
--     from
--         Orders o
--     join
--         Product p
--     on
--         o.product_id = p.product_id
--     where
--         date_format(order_date, '%Y-%m') = '2020-07'
--     group by
--         customer_id
--     having
--         sum(o.quantity * p.price) >= 100
-- )

-- select
--     c.customer_id,
--     c.name
-- from
--     june
-- join
--     july
-- on
--     june.customer_id = july.customer_id
-- join
--     Customers c
-- on
--     june.customer_id = c.customer_id



with cte as (
    select
        o.customer_id,
        o.product_id,
        o.quantity,
        o.order_date,
        p.price
    from
        Orders o
    left join
        Product p
    on
        o.product_id = p.product_id
),

june as (
    select
        customer_id
    from
        cte
    where
        year(order_date) = 2020
        and month(order_date) = 6
    group by
        customer_id
    having
        sum(quantity * price) >= 100
),

july as (
    select
        customer_id
    from
        cte
    where
        year(order_date) = 2020
        and month(order_date) = 7
    group by
        customer_id
    having
        sum(quantity * price) >= 100   
)

select
    c.customer_id,
    c.name
from
    Customers c
inner join
    june
on
    c.customer_id = june.customer_id
inner join
    july
on
    june.customer_id = july.customer_id

