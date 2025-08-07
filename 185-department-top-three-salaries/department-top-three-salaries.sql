-- with ranking as (
--     select
--         name,
--         departmentId,
--         salary,
--         dense_rank() over(partition by departmentId order by salary desc) as rnk
--     from
--         Employee
-- )

-- select
--     d.name as Department,
--     r.name as Employee,
--     r.salary as Salary
-- from
--     ranking r
-- join
--     Department d
-- on
--     r.departmentId = d.id
-- where
--     rnk <= 3 

with ranking as (
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
    r.name as Employee,
    r.salary as Salary
from
    ranking r
join
    Department d
on
    r.departmentId = d.id
where
    r.rnk <= 3