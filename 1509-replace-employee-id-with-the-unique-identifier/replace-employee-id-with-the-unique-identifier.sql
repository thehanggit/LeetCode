# Write your MySQL query statement below
-- select
--     EmployeeUNI.unique_id,
--     Employees.name
-- from
--     Employees
-- left join
--     EmployeeUNI
-- on
--     Employees.id = EmployeeUNI.id;



select
    U.unique_id,
    E.name
from
    Employees E
left join
    EmployeeUNI U
on
    E.id = U.id

