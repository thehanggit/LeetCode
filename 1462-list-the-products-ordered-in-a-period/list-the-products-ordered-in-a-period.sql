# Write your MySQL query statement below
select
    P.product_name,
    sum(O.unit) as unit
from
    Products P
left join
    Orders O
on
    P.product_id = O.product_id
where
    O.order_date between '2020-02-01' and '2020-02-29'
group by
    P.product_id
having
    sum(O.unit) >= 100
