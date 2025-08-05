# Write your MySQL query statement below
select
    id,
    month,
    sum(salary) over(partition by id order by month range between 2 preceding and current row) as salary
from
    Employee
where
    (id, month) not in (
        select
            id,
            max(month)
        from
            Employee
        group by
            id
    )
order by
    id,
    month desc