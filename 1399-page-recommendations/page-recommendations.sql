with user_1_friend as (
    select
        user1_id as id
    from
        Friendship
    where
        user2_id = 1
    union
    select
        user2_id id
    from
        Friendship
    where
        user1_id = 1
)

select
    distinct(l.page_id) as recommended_page
from
    Likes l
inner join
    user_1_friend u
on
    l.user_id = u.id
where
    l.page_id not in (select page_id from Likes where user_id = 1)
