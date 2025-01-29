# Write your MySQL query statement below
with rank_enro as (
    select
        *,
        dense_rank() over(partition by student_id order by grade desc, course_id) as rnk
    from
        Enrollments
)

select
    student_id,
    course_id,
    grade
from
    rank_enro
where
    rnk = 1
group by
    student_id