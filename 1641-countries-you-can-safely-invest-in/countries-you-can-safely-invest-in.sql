-- with personal_country_code as (
--     select
--         id,
--         name,
--         substring(phone_number, 1, 3) as country_code
--     from
--         Person
-- )

-- select
--     C.name as country
-- from
--     Country C
-- left join
--     person_country_code as P
-- on
--     C.country_code = P.country_code
-- left join
--     Calls CS
-- on
--     P.id in (CS.caller_id, CS.callee_id)
-- group by
--     C.name
-- having
--     avg(duration) > (select avg(duration) from Calls)


-- first get the country of each person id
-- calculate global average and country average call for each caller/callee
with country_person as (
    select
        p.id,
        c.name
    from
        Person p
    join
        Country c
    on
        substring(p.phone_number, 1, 3) = c.country_code
)

select
    cp.name as country
from
    country_person cp
join
    Calls c
on
    cp.id = c.caller_id or cp.id = c.callee_id
group by
    cp.name
having
    avg(c.duration) > (select avg(duration) from Calls)