with first_login as (
    select
        player_id,
        min(event_date) as first_login
    from
        Activity
    group by
        player_id
)

select
    round(count(fl.player_id)/ (select count(distinct player_id) from Activity),2) as fraction
from
    first_login fl
inner join
    Activity a
on
    fl.first_login = a.event_date - interval 1 day
    and fl.player_id = a.player_id

