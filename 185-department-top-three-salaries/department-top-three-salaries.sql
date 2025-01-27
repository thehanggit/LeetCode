# Write your MySQL query statement below
with department_name as (
    select
        E.*,
        D.name as Department
    from
        Employee E
    left join
        Department D
    on
        E.departmentId = D.id
),

with_rank as (
    select
        *,
        dense_rank() over(partition by departmentId order by salary desc) as rnk
    from
        department_name
)

select
    Department,
    name as Employee,
    salary as Salary
from
    with_rank
where
    rnk in (1,2,3)