# Write your MySQL query statement below
SELECT
    a.name AS Employee
From
    Employee as a,
    Employee as b
WHERE
    a.managerID = b.id
    AND a.salary > b.salary
;