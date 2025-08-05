# Write your MySQL query statement below
with cte as (
    select
        *,
        sum(frequency) over(order by num) as total_freq,
        (sum(frequency) over())/2.0 as median_index
    from
        Numbers
)

select
    round(avg(num),1) as median
from
    cte
where
    median_index between (total_freq - frequency) and total_freq