-- with cte1 as (
--     select
--         u.name,
--         count(distinct mr.movie_id) as num_movies
--     from
--         MovieRating mr
--     join
--         Users u
--     on
--         mr.user_id = u.user_id
--     group by
--         u.name
--     order by
--         num_movies desc, u.name
--     limit
--         1
-- ),

-- cte2 as (
--     select
--         m.title,
--         avg(mr.rating) as highest_rating
--     from
--         MovieRating mr
--     join
--         Movies m
--     on
--         mr.movie_id = m.movie_id
--     where
--         year(mr.created_at) = 2020 and month(mr.created_at) = 2
--     group by
--         m.title
--     order by
--         highest_rating desc, title
--     limit
--         1
-- )

-- select
--     name as results
-- from
--     cte1
-- union all
-- select
--     title as results
-- from
--     cte2

with cte1 as (
    select
        u.name as results
    from
        MovieRating m
    left join
        Users u
    on
        m.user_id = u.user_id
    group by
        m.user_id
    order by
        count(m.movie_id) desc,
        u.name
    limit
        1
),

cte2 as (
    select
        mv.title
    from
        MovieRating m
    left join
        Movies mv
    on
        m.movie_id = mv.movie_id
    where
        date_format(created_at, '%Y-%m') = '2020-02'
    group by
        m.movie_id
    order by
        avg(m.rating) desc,
        mv.title
    limit
        1
)

select
    *
from
    cte1
union all
select
    *
from
    cte2
