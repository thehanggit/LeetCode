# Write your MySQL query statement below
-- select
--     s.student_id,
--     s.student_name,
--     sub.subject_name,
--     ifnull(grouped.attended_exams, 0) as attended_exams
-- from
--     Students s
-- cross join
--     Subjects sub
-- left join (
--     select
--         student_id,
--         subject_name,
--         count(*) as attended_exams
--     from
--         Examinations
--     group by
--         student_id,
--         subject_name
-- ) grouped
-- on
--     s.student_id = grouped.student_id
--     and sub.subject_name = grouped.subject_name
-- order by s.student_id, sub.subject_name

with cross_table as (
    select
        S.*,
        Sub.*
    from
        Students S
    cross join
        Subjects Sub
),

calculate_exam as (
    select
        student_id,
        subject_name,
        count(*) as attended_exams
    from
        Examinations
    group by
        student_id,
        subject_name
)

select
    C.student_id,
    C.student_name,
    C.subject_name,
    ifnull (E.attended_exams, 0) as attended_exams
from
    cross_table C
left join
    calculate_exam E
on
    C.student_id = E.student_id
    and C.subject_name = E.subject_name
order by
    C.student_id, C.subject_name

