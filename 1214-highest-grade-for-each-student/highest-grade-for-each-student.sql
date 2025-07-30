with grade_rank as (
    select
        student_id,
        course_id,
        grade,
        rank() over(partition by student_id order by grade desc, course_id asc) as ranking
    from
        Enrollments
)

select
    student_id,
    course_id,
    grade
from
    grade_rank
where
    ranking = 1
order by
    student_id