-- select
--     email as Email
-- from
--     Person
-- group by
--     email
-- having
--     count(email) >= 2

select
    email
from
    Person
group by
    email
having
    count(id) > 1 