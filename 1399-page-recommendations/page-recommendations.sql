-- with user_1_friend as (
--     select
--         case
--             when user1_id = 1 then user2_id
--             when user2_id = 1 then user1_id
--         end as id
--     from
--         Friendship
-- )

-- select
--     distinct(l.page_id) as recommended_page
-- from
--     Likes l
-- inner join
--     user_1_friend u
-- on
--     l.user_id = u.id
-- where
--     l.page_id not in (select page_id from Likes where user_id = 1)


-- find out friends of user_id = 1
-- recommend pages of 1's friends liked page_id
with friends as (
    select
        case
            when user1_id = 1 then user2_id
            when user2_id = 1 then user1_id
        end as friend
    from
        Friendship
)

select distinct
    l.page_id as recommended_page
from
    Likes l
join
    friends f
on
    l.user_id = f.friend
where
    l.page_id not in (
        select
            page_id
        from
            Likes
        where
            user_id = 1
    )
