# Write your MySQL query statement below
with rnk as (
    select
        username,
        startDate,
        rank() over(partition by username order by startDate desc) as rnk,
        count(activity) over(partition by username) as cnt
    from
        UserActivity
)

select
    u.*
from
    UserActivity u
join
    rnk r
on
    u.username = r.username
    and u.startDate = r.startDate
where
    r.rnk = 2
    or r.cnt = 1