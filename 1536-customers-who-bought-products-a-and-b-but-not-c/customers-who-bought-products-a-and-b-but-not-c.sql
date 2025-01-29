# Write your MySQL query statement below
with customer_id_buy_c as (
    select
        customer_id
    from
        Orders
    group by
        customer_id
    having
        sum(product_name='A') > 0
        and sum(product_name='B') > 0
        and sum(product_name='C') = 0
)

select
    *
from
    Customers
where
    customer_id in (
        select
            customer_id
        from
            customer_id_buy_c
    )

