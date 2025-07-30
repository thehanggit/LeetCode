
select
    c.*
from
    Orders o
inner join
    Customers c
on
    o.customer_id = c.customer_id
group by
    o.customer_id
having
    sum(product_name='A') >= 1
    and sum(product_name='B') >= 1
    and sum(product_name='C') = 0
order by
    o.customer_id