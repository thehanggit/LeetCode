# Write your MySQL query statement below
With orders_red as (
    select
        O.sales_id
    from
        Orders O
    left join
        Company C
    on
        O.com_id = C.com_id
    where
        C.name = 'RED'
)

select
    name
from
    SalesPerson
where
    sales_id not in (
        select
            sales_id
        from
            orders_red
    )