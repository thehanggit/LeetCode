-- # Write your MySQL query statement below
-- with row_Weather as (
--     select
--         *,
--         lag(temperature, 1) over (order by recordDate) as previous_temp,
--         lag(recordDate, 1) over (order by recordDate) as previous_record
--     from
--         Weather
-- )

-- select
--     id
-- from
--     row_Weather
-- where
--     temperature > previous_temp
-- and
--     recordDate = date_add(previous_record, interval 1 day)

with previous_date as (
    select
        *,
        lag(temperature, 1) over (order by recordDate) as previous_temp,
        lag(recordDate, 1) over (order by recordDate) as previous_date
    from
        Weather
)

select
    id
from
    previous_date
where
    temperature > previous_temp
    and previous_date = date_sub(recordDate, interval 1 day)

