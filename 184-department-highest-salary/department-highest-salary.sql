-- select
--     d.name as Department,
--     e.name as Employee,
--     e.salary as Salary
-- from
--     Employee e
-- left join
--     Department d
-- on
--     e.departmentId = d.id
-- where
--     (e.departmentId, e.salary) in (
--         select
--             departmentId,
--             max(salary)
--         from
--             Employee
--         group by
--             departmentId
--     )

with cte as (
    select
        name,
        salary,
        departmentId,
        dense_rank() over(partition by departmentId order by salary desc) as rnk
    from
        Employee
)

select
    d.name as Department,
    c.name as Employee,
    c.salary as Salary
from
    cte c
join
    Department d
on
    c.departmentId = d.id
where
    c.rnk = 1