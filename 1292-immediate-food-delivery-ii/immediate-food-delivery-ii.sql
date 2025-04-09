with first_order_date as (
    select
        customer_id,
        min(order_date) as first_order_date
    from
        Delivery
    group by
        customer_id
),

order_category as (
    select
        f.customer_id,
        case
            when d.order_date = d.customer_pref_delivery_date then "immediate"
            else "scheduled"
        end as order_category
    from
        first_order_date f
    inner join
        Delivery d
    on
        f.customer_id = d.customer_id
        and f.first_order_date = d.order_date
)

-- select * from order_category

select
    round(100*sum(case when order_category = "immediate" then 1 else 0 end) * 1.0/ count(*),2) as immediate_percentage
from
    order_category
