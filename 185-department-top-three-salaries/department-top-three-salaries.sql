with ranking as (
    select
        departmentId,
        name,
        salary,
        dense_rank() over(partition by departmentId order by salary desc) as ranking
    from
        Employee
)

select
    d.name as Department,
    r.name as Employee,
    salary as Salary
from
    ranking r
join
    Department d
on
    r.departmentId = d.id
where
    ranking <= 3
