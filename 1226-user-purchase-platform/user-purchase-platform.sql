# Write your MySQL query statement below
with base as (
    select
        user_id,
        spend_date,
        sum(case when platform = 'mobile' then amount else 0 end) as mobile,
        sum(case when platform = 'desktop' then amount else 0 end) as desktop
    from
        Spending
    group by
        user_id,
        spend_date
),

info as (
    select
        spend_date,
        user_id,
        mobile + desktop as total_amount,
        case
            when mobile > 0  and desktop > 0 then 'both'
            when mobile > 0 and desktop = 0 then 'mobile'
            when mobile = 0 and desktop > 0 then 'desktop'
        end as platform
    from
        base
),

build_table as (
    select
        distinct spend_date,
        'desktop' as platform
    from
        Spending
    union
    select
        distinct spend_date,
        'mobile' as platform
    from
        Spending
    union
    select
        distinct spend_date,
        'both' as platform
    from
        Spending
)

select
    b.spend_date,
    b.platform,
    ifnull(sum(total_amount), 0) as total_amount,
    ifnull(count(distinct user_id), 0) as total_users
from
    build_table b
left join
    info i
on
    b.spend_date = i.spend_date
    and b.platform = i.platform
group by
    b.spend_date,
    b.platform


