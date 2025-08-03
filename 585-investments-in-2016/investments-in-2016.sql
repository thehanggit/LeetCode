# Write your MySQL query statement below
with cte as (
    select
        tiv_2016,
        count(*) over (partition by tiv_2015) as tiv_2015_cnt,
        count(*) over (partition by lat, lon) as lat_lon_cnt
    from
        insurance
)

select
    round(sum(tiv_2016),2) as tiv_2016
from
    cte
where
    tiv_2015_cnt > 1
    and lat_lon_cnt = 1

-- with cte as (
--     select
--         tiv_2016,
--         count(*) over(partition by tiv_2015) as tiv_2015_cnt,
--         count(*) over(partition by (lat, lon)) as lat_lon_cnt
--     from
--         Insurance
-- )

-- select
--     round(sum(tiv_2016), 2)
-- from
--     cte
-- where
--     tiv_2015_cnt > 1
--     and lat_lon_cnt = 1
