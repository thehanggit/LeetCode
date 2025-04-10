with ranking as (
    select
        customer_id,
        product_id,
        rank() over(partition by customer_id order by count(product_id) desc) as ranking
    from
        Orders
    group by
        customer_id, product_id
)

select
    r.customer_id,
    p.product_id,
    p.product_name
from
    ranking r
join
    Products p
on
    r.product_id = p.product_id
where
    r.ranking = 1