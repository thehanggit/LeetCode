# Write your MySQL query statement below
with counts as (
    select
        count(*) as counts
    from
        Seat
)

select
    case
        when mod(S.id, 2) !=0 and S.id != C.counts then id + 1
        when mod(S.id, 2) !=0 and S.id = C.counts then id
        else id - 1
    end as id,
    student
from
    Seat S,
    counts C
order by
    id asc

