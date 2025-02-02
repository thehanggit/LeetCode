# Write your MySQL query statement below
with project_info as (
    select
        P.project_id,
        E.*
    from
        Employee E
    left join
        Project P
    on
        P.employee_id = E.employee_id
)

select
    project_id,
    employee_id
from
    project_info
where
    (project_id, experience_years) in (
        select
            project_id,
            max(experience_years) as most_experience
        from
            project_info
        group by
            project_id
        
    )