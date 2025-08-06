# Write your MySQL query statement below
select
    d.dept_name,
    ifnull(count(distinct s.student_id), 0) as student_number
from
    Department d
left join
    Student s
on
    s.dept_id = d.dept_id
group by
    d.dept_id
order by
    student_number desc,
    d.dept_name 
