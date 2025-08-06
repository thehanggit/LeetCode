# Write your MySQL query statement below
with base as (
    select
        player_id,
        min(event_date) as install_dt
    from
        Activity
    group by
        player_id
),

retention as (
    select
        *,
        case
            when (player_id, date_add(install_dt, interval 1 day)) in (select player_id, event_date from Activity) then 1
            else 0
        end as retention
    from
        base
)

select
    install_dt,
    count(*) as installs,
    round(sum(retention)/count(*), 2) as Day1_retention
from
    retention
group by
    install_dt

