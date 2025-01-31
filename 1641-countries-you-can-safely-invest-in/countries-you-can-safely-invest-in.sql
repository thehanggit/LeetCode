# Write your MySQL query statement below
with person_country_code as (
    select
        *,
        substring(phone_number, 1, 3) as  country_code
    from
        Person
)

select
    C.name as country
from
    Country C
left join
    person_country_code as P
on
    C.country_code = P.country_code
left join
    Calls CS
on
    P.id in (CS.caller_id, CS.callee_id)
group by
    C.name
having
    avg(duration) > (select avg(duration) from Calls)