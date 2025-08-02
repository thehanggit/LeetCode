-- select
--     w1.id as Id
-- from
--     Weather w1,
--     Weather w2
-- where
--     w1.recordDate = w2.recordDate + interval 1 day
-- and
--     w1.temperature > w2.temperature

select
    w1.id as id
from
    Weather w1
join
    Weather w2
on
    datediff(w1.recordDate, w2.recordDate) = 1
where
    w1.temperature > w2.temperature