-- select
--     u.name,
--     sum(amount) as balance
-- from
--     Transactions t
-- join
--     Users u
-- on
--     t.account = u.account
-- group by
--     t.account
-- having
--     sum(amount) > 10000


select
    u.name,
    sum(t.amount) as balance
from
    Users u
left join
    Transactions t
on
    u.account = t.account
group by
    t.account
having
    balance > 10000
