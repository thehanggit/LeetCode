with start_cte as (
    select
        machine_id,
        process_id,
        timestamp
    from
        Activity
    where
        activity_type = 'start'
),

end_cte as (
    select
        machine_id,
        process_id,
        timestamp
    from
        Activity
    where
        activity_type = 'end'
),

cte as (
    select
        s.machine_id,
        s.process_id,
        e.timestamp - s.timestamp as time
    from
        start_cte s
    join
        end_cte e
    on
        s.machine_id = e.machine_id
        and s.process_id = e.process_id
)

select
    machine_id,
    round(avg(time), 3) as processing_time
from
    cte
group by
    machine_id