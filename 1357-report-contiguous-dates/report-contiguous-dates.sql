# Write your MySQL query statement below
with all_info as (
    select
        fail_date as date,
        'failed' as period_state
    from
        Failed
    union all

    select
        success_date as date,
        'succeeded' as period_state
    from
        Succeeded
),

rnk as (
    select
        date,
        period_state,
        row_number() over(order by period_state, date) as seq
    from
        all_info
    where
        date between '2019-01-01' and '2019-12-31'
),

c as (
    select
        date,
        period_state,
        seq,
        date_sub(date, interval seq day) as seqStart
    from
        rnk
)

select
    period_state,
    min(date) as start_date,
    max(date) as end_date
from
    c
group by
    seqStart,
    period_state
order by
    start_date