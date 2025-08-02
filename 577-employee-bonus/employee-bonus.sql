-- select
--     e.name,
--     b.bonus
-- from
--     Employee e
-- left join
--     Bonus b
-- on
--     b.empId = e.empId
-- where
--     b.bonus < 1000 or b.bonus is null

select
    e.name,
    b.bonus
from
    Employee e
left join
    Bonus b
on
    e.empId = b.empId
where
    bonus < 1000 or bonus is null