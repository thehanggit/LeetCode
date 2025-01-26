# Write your MySQL query statement below
with finance as (
    select
        distinct visited_on,
        sum(amount) over (order by visited_on range between interval 6 day preceding and current row) amount,
        min(visited_on) over() 1st_date
    from
        Customer
)

select
    visited_on,
    amount,
    round(amount/7, 2) as average_amount
from
    finance
where
    visited_on >= date_add(1st_date, interval 6 day)