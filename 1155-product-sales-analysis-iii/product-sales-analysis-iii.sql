-- select
--     product_id,
--     year as first_year,
--     sum(quantity) as quantity,
--     price
-- from
--     Sales
-- where
--     (product_id, year) in (
--         select
--             product_id,
--             min(year) as first_year
--         from
--             Sales
--         group by
--             product_id
--     )
-- group by
--     product_id, year, price
 

 select
    product_id,
    year as first_year,
    quantity,
    price
 from
    Sales
where
    (product_id, year) in (
        select
            product_id,
            min(year)
        from
            Sales
        group by
            product_id
    )