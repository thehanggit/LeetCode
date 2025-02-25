with cte as (
    select
        customer_id,
        min(order_date) as first_order
    from
        Delivery 
    group by
        customer_id
)

select
    round(100*sum(case when d.order_date = d.customer_pref_delivery_date then 1 else 0 end)* 1.0 / count(*), 2) as immediate_percentage
from
    cte c
join
    Delivery d
on
    c.customer_id = d.customer_id
    and c.first_order = d.order_date