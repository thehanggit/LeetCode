# Write your MySQL query statement below
-- select
--     customer_name,
--     customer_id,
--     order_id,
--     order_date
-- from
--     (select
--         C.name as customer_name,
--         O.customer_id,
--         O.order_id,
--         O.order_date,
--         rank() over(partition by O.customer_id order by O.order_date desc) as rnk
--     from
--         Orders O
--     left join
--         Customers C
--     on
--         O.customer_id = C.customer_id) temp
-- where
--     rnk <= 3
-- order by
--     customer_name, customer_id, order_date desc



with ranking_order as (
    select
        customer_id,
        order_id,
        order_date,
        rank() over(partition by customer_id order by order_date desc) as recent_rank
    from
        Orders
)

select
    c.name as customer_name,
    r.customer_id,
    r.order_id,
    r.order_date
from
    ranking_order r
left join
    Customers c
on
    r.customer_id = c.customer_id
where
    r.recent_rank <= 3
order by
    c.name, r.customer_id, r.order_date desc


-- with cte as (
--     select
--         order_id,
--         customer_id,
--         order_date,
--         rank() over(partition by customer_id order by order_date desc) as rnk
--     from
--         Orders
    
-- )

-- select
--     c.name as customer_name,
--     e.customer_id,
--     e.order_id,
--     e.order_date
-- from
--     cte e
-- left join
--     Customers c
-- on
--     e.customer_id = c.customer_id
-- where
--     e.rnk <= 3
-- order by
--     customer_name,
--     e.customer_id,
--     e.order_date desc




















