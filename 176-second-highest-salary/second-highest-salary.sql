-- # Write your MySQL query statement below
-- SELECT (
--     SELECT DISTINCT Salary
--     FROM Employee 
--     ORDER BY Salary DESC
--     LIMIT 1 OFFSET 1)
-- AS SecondHighestSalary

select (
    select distinct salary
    from Employee
    order by salary desc
    limit 1
    offset 1
) as SecondHighestSalary

