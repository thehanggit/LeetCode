# Write your MySQL query statement below
select
    S.seller_name
from
    Seller S
left join
    (
        select
            distinct seller_id
        from
            Orders
        where
            year(sale_date) = 2020
    ) O
on
    S.seller_id = O.seller_id
where
    O.seller_id is null
order by
    S.seller_name