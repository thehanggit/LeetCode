-- select
--     id,
--     name
-- from
--     Students
-- where
--     department_id not in (
--         select
--             id
--         from
--             Departments
--     )

select
    id,
    name
from
    Students
where
    department_id not in (
        select
            id
        from
            Departments
    )