with cte as (
    select
        from_id as person1,
        to_id as person2,
        count(*) as call_count,
        sum(duration) as total_duration
    from
        Calls
    where
        from_id < to_id
    group by
        person1, person2
    union all
    select
        to_id as person1,
        from_id as person2,
        count(*) as call_count,
        sum(duration) as total_duration
    from
        Calls
    where
        from_id > to_id
    group by
        person1, person2
)

select
    person1,
    person2,
    sum(call_count) as call_count,
    sum(total_duration) as total_duration
from
    cte
group by
    person1, person2
