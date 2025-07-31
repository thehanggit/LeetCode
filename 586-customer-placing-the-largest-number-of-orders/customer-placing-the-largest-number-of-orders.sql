-- select
--     customer_number
-- from
--     orders
-- group by
--     customer_number
-- order by
--     count(order_number) desc
-- limit
--     1

-- select
--     customer_number
-- from
--     orders
-- group by
--     customer_number
-- order by
--     count(order_number) desc
-- limit
--     1
with cte as (
    select
        customer_number,
        rank() over(order by count(order_number) desc) as ranking
    from
        Orders
    group by
        customer_number
)

select
    customer_number
from
    cte
where
    ranking = 1