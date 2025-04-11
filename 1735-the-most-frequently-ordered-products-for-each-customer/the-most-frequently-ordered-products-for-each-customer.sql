with cte as(
    select
        customer_id,
        product_id,
        rank() over(partition by customer_id order by count(*) desc) ranking
    from
        Orders
    group by
        customer_id, product_id
)

select
    c.customer_id,
    c.product_id,
    p.product_name
from
    cte c
left join
    Products p
on
    c.product_id = p.product_id
where
    ranking = 1

