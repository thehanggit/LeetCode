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

select
    E.name
from
    Employee E
join
    Employee M
on
    E.id = M.managerId
group by
    E.id, E.name
having
    count(M.managerId) >= 5
