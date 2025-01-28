# Write your MySQL query statement below
-- select
--     e1.name
-- from
--     employee e1
-- join
--     (select
--         managerId
--     from
--         employee
--     group by
--         managerId
--     having
--         count(managerId) >= 5
--     ) e2
-- where
--     e1.id = e2.managerId

with reports_manager as (
    select
        managerId,
        count(*) as reports
    from
        Employee
    group by
        managerId
)

select
    E.name
from
    reports_manager R
inner join
    Employee E
on
    R.managerId = E.id
where
    R.reports >= 5