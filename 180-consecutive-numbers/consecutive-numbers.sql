# Write your MySQL query statement below
-- SELECT DISTINCT
--     l1.num AS ConsecutiveNums
-- FROM 
--     Logs l1,
--     Logs l2,
--     Logs l3
-- WHERE
--     l1.id = l2.id - 1
--     AND l2.id = l3.id - 1
--     AND l1.num = l2.num
--     AND l2.num = l3.num
-- ;

select
    distinct L1.num as ConsecutiveNums
from
    logs L1,
    Logs L2,
    Logs L3
where
    L1.id = L2.id - 1
    and L2.id = L3.id - 1
    and L1.num = L2.num
    and L2.num = L3.num

