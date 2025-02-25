with first_login as (
    select
        player_id,
        min(event_date) as first_date
    from
        Activity
    group by
        player_id
),

cte as (
select
    f.player_id
from
    first_login f
join
    Activity a2
on
    f.player_id = a2.player_id
    and f.first_date = a2.event_date - interval 1 day
)

select
    round((select count(*) from cte) / count(distinct player_id), 2) as fraction
from
    Activity