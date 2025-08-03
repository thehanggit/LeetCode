select
    max(num) as num
from
    MyNumbers
group by
    num
having
    count(*) = 1
union all
select
    null
order by 
    num desc
limit
    1