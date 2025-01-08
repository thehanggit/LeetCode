CREATE FUNCTION getNthhighestSalary(N INT) RETURNS INT
BEGIN
DECLARE p INT;
SET p = N - 1;
RETURN (
    Select
             *
    FROM
        (
            SELECT DISTINCT
            salary
            FROM Employee
            ORDER BY salary DESC
            LIMIT 1 OFFSET p
        ) AS getNthHighestSalary
);
END

