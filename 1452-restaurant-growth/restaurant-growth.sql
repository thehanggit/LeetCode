-- with finance as (
--     select
--         distinct visited_on,
--         sum(amount) over (order by visited_on range between interval 6 day preceding and current row) as amount,
--         min(visited_on) over () as 1st_date
--     from
--         Customer
-- )

-- select
--     visited_on,
--     amount,
--     round(amount/7 ,2) as average_amount
-- from
--     finance
-- where
--     1st_date <= visited_on - interval 6 day
-- order by
--     visited_on


with finance as (
    select
        distinct visited_on,
        sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as amount,
        min(visited_on) over() as 1st_day
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
    1st_day <= visited_on - interval 6 day
