# Write your MySQL query statement below
-- select distinct
--     c1.seat_id
-- from
--     Cinema c1
-- join
--     Cinema c2
-- on
--     abs(c1.seat_id - c2.seat_id) = 1
--     and c1.free
--     and c2.free
-- order by
--     c1.seat_id

select distinct
    c1.seat_id
from
    Cinema c1
join
    Cinema c2
on
    abs(c1.seat_id - c2.seat_id) = 1
    and c1.free
    and c2.free
order by
    c1.seat_id