-- (Exercício 1) Crie uma coluna calculada com o número de visitas realizadas por cada
-- cliente da tabela sales.customers
with visitas as (
	select customer_id, count(*) as nvisitas
	from sales.funnel
	group by customer_id
)
select cus.*, nvisitas
from sales.customers as cus
left join visitas as vis
	on cus.customer_id=vis.customer_id