select
    s.user_id,
    case when c.action is not null then round(sum(case when c.action = 'confirmed' then 1 else 0 end) * 1.0 / sum(case when c.action is not null then 1 else 0 end), 2) else 0 end as confirmation_rate
from
    Signups s
left join
    Confirmations c
on
    c.user_id = s.user_id
group by
    s.user_id