-- with first_order_date as (
--     select
--         customer_id,
--         min(order_date) as first_order_date
--     from
--         Delivery
--     group by
--         customer_id
-- ),

-- order_category as (
--     select
--         f.customer_id,
--         case
--             when d.order_date = d.customer_pref_delivery_date then "immediate"
--             else "scheduled"
--         end as order_category
--     from
--         first_order_date f
--     inner join
--         Delivery d
--     on
--         f.customer_id = d.customer_id
--         and f.first_order_date = d.order_date
-- )

-- -- select * from order_category

-- select
--     round(100*sum(case when order_category = "immediate" then 1 else 0 end) * 1.0/ count(*),2) as immediate_percentage
-- from
--     order_category


-- have a column to tell whether this order is immediate or not
-- find the earliest order for each customoer
-- inner join these two to get the final answer

with cte as (
    select
        customer_id,
        min(order_date) as first_order
    from
        Delivery
    group by
        customer_id
),

order_category as (
    select
        c.customer_id,
        case when d.order_date = d.customer_pref_delivery_date then 'immediate' else 'scheduled' end as order_type
    from
        cte c
    join
        Delivery d
    on
        c.customer_id = d.customer_id
        and c.first_order = d.order_date
)

select
    round(100*sum(case when order_type = 'immediate' then 1 else 0 end) / count(*),2) as immediate_percentage
from
    order_category
