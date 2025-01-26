# Write your MySQL query statement below
-- with income_category as (
--     select
--         income,
--         case
--             when income < 20000
--                 then 'Low Salary'
--             when income >= 20000 and income <= 50000
--                 then 'Average Salary'
--             when income > 50000
--                 then 'High Salary'
--         end as category
--     from
--         Accounts
-- )

-- select
--     category,
--     count(category) as accounts_count
-- from
--     income_category
-- group by
--     category

SELECT
    c.category,
    COUNT(a.income) AS accounts_count
FROM
    (SELECT 'Low Salary' AS category
     UNION ALL
     SELECT 'Average Salary'
     UNION ALL
     SELECT 'High Salary') AS c
LEFT JOIN Accounts a ON
    ( (c.category = 'Low Salary' AND a.income < 20000) OR
      (c.category = 'Average Salary' AND a.income BETWEEN 20000 AND 50000) OR
      (c.category = 'High Salary' AND a.income > 50000) )
GROUP BY
    c.category
-- ORDER BY
--     FIELD(c.category, 'Low Salary', 'Average Salary', 'High Salary');
