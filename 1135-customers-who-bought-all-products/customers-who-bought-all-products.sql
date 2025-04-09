with num_keys as (
    select
        customer_id,
        count(distinct product_key) as num
    from
        Customer
    group by
        customer_id
)

select
    customer_id
from
    num_keys
where
    num = (select count(*) from Product)