# Write your MySQL query statement below
select
    P.product_name,
    O.product_id,
    O.order_id,
    O.order_date
from
    Orders O
left join
    Products P
on
    O.product_id = P.product_id
where
    (O.product_id, O.order_date) in (
        select
            product_id,
            max(order_date)
        from
            Orders
        group by
            product_id
    )
order by
    P.product_name, O.product_id, O.order_id