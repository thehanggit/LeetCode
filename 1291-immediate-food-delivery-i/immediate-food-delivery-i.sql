# Write your MySQL query statement below
-- with delivery_cate as (
--     select
--         delivery_id,
--         case
--             when order_date = customer_pref_delivery_date then 'immediate'
--             when order_date < customer_pref_delivery_date then 'scheduled'
--         end as category
--     from
--         Delivery
-- )

-- select
--     round(avg(category = 'immediate') * 100, 2) as immediate_percentage
-- from
--     delivery_cate

select
    round(100 * avg(order_date = customer_pref_delivery_date), 2) as immediate_percentage
from
    Delivery