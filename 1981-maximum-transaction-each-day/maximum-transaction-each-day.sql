with ranking as (
    select
        transaction_id,
        rank() over(partition by date(day) order by amount desc) as ranking
    from
        Transactions
)

select
    transaction_id
from
    ranking
where
    ranking = 1
order by
    transaction_id

