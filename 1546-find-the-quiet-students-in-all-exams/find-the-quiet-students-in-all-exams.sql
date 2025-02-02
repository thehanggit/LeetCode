# Write your MySQL query statement below
with exam_score_range as (
    select
        exam_id,
        min(score) as min_score,
        max(score) as max_score
    from
        Exam   
    group by
        exam_id
),

exam_info as (
    select
        exam_id,
        min_score as score
    from
        exam_score_range
    union
    select
        exam_id,
        max_score as score
    from
        exam_score_range
),

non_quiet_student as (
    select
        distinct student_id
    from
        (
            select
                student_id
            from
                Exam
            where
                (exam_id, score) in (
                    select
                        exam_id,
                        score
                    from
                        exam_info
                )
        )as temp
)

select distinct
    E.student_id,
    S.student_name
from
    Exam E
left join
    Student S
on
    E.student_id = S.student_id
where
    E.student_id not in (
        select
            student_id
        from
            non_quiet_student
    )
order by
    E.student_id
