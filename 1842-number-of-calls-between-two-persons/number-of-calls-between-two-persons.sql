# Write your MySQL query statement below
with distinct_pair as (
    select
        case
            when from_id < to_id then from_id
            when from_id > to_id then to_id
        end as person1,
        case
            when from_id < to_id then to_id
            when from_id > to_id then from_id
        end as person2,
        duration
    from
        Calls
)

select
    person1,
    person2,
    count(*) as call_count,
    sum(duration) as total_duration
from
    distinct_pair
group by
    person1, person2