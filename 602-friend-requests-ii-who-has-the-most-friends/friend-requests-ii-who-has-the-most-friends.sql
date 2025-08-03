with friends as (
    select
        requester_id as id,
        count(*) as friend_num
    from
        RequestAccepted
    group by
        requester_id
    union all
    select
        accepter_id as id,
        count(*) as friend_num
    from
        RequestAccepted
    group by
        accepter_id
)

select
    id,
    sum(friend_num) as num
from
    friends
group by
    id
order by
    num desc
limit 1