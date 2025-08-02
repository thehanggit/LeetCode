with cte as (
    select
        *
    from
        Students
    cross join
        Subjects
)

select
    c.*,
    case when e.subject_name is not null then count(*) else 0 end as attended_exams
from
    cte c
left join
    Examinations e
on
    c.student_id = e.student_id
    and c.subject_name = e.subject_name
group by
    c.student_id,
    c.subject_name
order by
    c.student_id,
    c.subject_name
