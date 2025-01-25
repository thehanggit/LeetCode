# Write your MySQL query statement below
with num_count as (
    select
        num,
        count(num) as frequency
    from
        MyNumbers
    group by num
)

select
    max(num) as num
from
    num_count
where
    frequency = 1