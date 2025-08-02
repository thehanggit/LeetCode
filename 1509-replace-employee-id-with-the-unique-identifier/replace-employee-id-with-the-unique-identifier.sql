-- select
--     e.name,
--     ei.unique_id
-- from
--     Employees e
-- left join
--     EmployeeUNI ei
-- on
--     e.id = ei.id

select
    u.unique_id,
    e.name
from
    Employees e
left join
    EmployeeUNI u
on
    e.id = u.id