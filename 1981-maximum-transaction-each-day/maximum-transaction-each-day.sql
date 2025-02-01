# Write your MySQL query statement below
with temp as (
    select
        date(day) as day_time,
        max(amount) as max_tran
    from
        Transactions
    group by
        day_time
)

select distinct
    T.transaction_id
from
    Transactions T
join
    temp t
on
    T.max_tran = t.amount
    and T.day_time = date(t.day)
order by
    T.transaction_id