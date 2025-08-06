# Write your MySQL query statement below
-- answer rate = number of answers / number of questions shown in this table
with answer_rate as (
    select
        question_id,
        sum(case when answer_id is not null then 1 else 0 end) / sum(case when action = 'show' then 1 else 0 end) as answer_rate
    from
        SurveyLog
    group by
        question_id
)

select
    question_id as survey_log
from
    answer_rate
order by
    answer_rate desc,
    question_id
limit
    1