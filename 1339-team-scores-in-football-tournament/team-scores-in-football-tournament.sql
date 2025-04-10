with match_points as (
    select
        host_team as team,
        case
            when host_goals > guest_goals then 3
            when host_goals = guest_goals then 1
            else 0
        end as points
    from
        Matches
    union all
    select
        guest_team as team,
        case
            when host_goals < guest_goals then 3
            when host_goals = guest_goals then 1
            else 0
        end as points
    from
        Matches
)

select
    t.team_id,
    t.team_name,
    ifnull(sum(points), 0) as num_points
from
    Teams t
left join
    match_points mp
on
    mp.team = t.team_id
group by
    t.team_id, t.team_name
order by
    num_points desc, t.team_id asc