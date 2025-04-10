select
    E.left_operand,
    E.operator,
    E.right_operand,
    case
        when E.operator = ">" and V1.value > V2.value then "true"
        when E.operator = "=" and V1.value = V2.value then "true"
        when E.operator = "<" and V1.value < V2.value then "true"
        else "false"
    end as value
from
    Expressions E
join Variables V1 on E.left_operand = V1.name
join Variables V2 on E.right_operand = V2.name

