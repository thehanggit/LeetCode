# Write your MySQL query statement below
with frequency as (
    select
        customer_id,
        product_id,
        rank() over(partition by customer_id order by count(product_id) desc) as rnk
    from
        Orders
    group by
        customer_id, product_id
)

select
    F.customer_id,
    F.product_id,
    P.product_name
from
    frequency F
left join
    Products P
on
    F.product_id = P.product_id
where
    F.rnk = 1
