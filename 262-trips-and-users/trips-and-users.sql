# Write your MySQL query statement below
-- cancellation rate = number of requests = cancelled_by_driver, cancelled_by_client / number of request
select
    request_at as Day,
    round(sum(case when status in ('cancelled_by_driver', 'cancelled_by_client') then 1 else 0 end) / count(*), 2) as "Cancellation Rate"
from
    Trips
where
    client_id in (select users_id from Users where banned = 'No' and role = 'client')
    and driver_id in (select users_id from Users where banned = 'No' and role = 'driver')
    and request_at between '2013-10-01' and '2013-10-03'
group by
    request_at
having
    count(*) > 0

