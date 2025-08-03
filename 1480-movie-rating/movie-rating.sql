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
