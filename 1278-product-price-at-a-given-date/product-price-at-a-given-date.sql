# Write your MySQL query statement below
-- select
--     product_id,
--     case
--         when
--             max(change_date) <= '2019-08-16' then new_price else 10
--     end as price
-- from
--     Products
-- group by
--     product_id

-- select
--     product_id,
--     10 as price
-- from
--     Products
-- group by
--     product_id
-- having
--     min(change_date) > '2019-08-16'
-- union all
-- select
--     product_id,
--     new_price as price
-- from
--     Products
-- where
--     (product_id, change_date) in (
--         select
--             product_id,
--             max(change_date)
--         from
--             Products
--         where
--             change_date <= '2019-08-16'
--         group by
--             product_id
--     )

with unique_products as (
    select
        distinct product_id
    from
        Products
),

first_price as (
    select
        distinct product_id,
        first_value (new_price) over (partition by (product_id) order by change_date desc) as price
    from
        Products
    where
        change_date <= '2019-08-16'
)

select
    up.product_id,
    ifnull (fp.price, 10) as price
from
    unique_products as up
left join
    first_price as fp
on
    up.product_id = fp.product_id
