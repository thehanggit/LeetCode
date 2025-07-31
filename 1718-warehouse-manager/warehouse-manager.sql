-- with volume_product as (
--     select
--         product_id,
--         Width * Length * Height as unit_volume
--     from
--         Products
-- )

-- select
--     w.name as warehouse_name,
--     sum(v.unit_volume * w.units) as volume
-- from
--     Warehouse w
-- join
--     volume_product v
-- on
--     w.product_id = v.product_id
-- group by
--     w.name


-- calculate the unit volume for each product
-- sum the volumes for each warehosue

with unit_volume as (
    select
        product_id,
        Width * Length * Height as unit_volume
    from
        Products
)

select
    w.name as warehouse_name,
    sum(w.units * u.unit_volume) as volume
from
    Warehouse w
left join
    unit_volume u
on
    w.product_id = u.product_id
group by
    w.name