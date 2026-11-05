-- 코드를 입력하세요
select p.product_id, p.product_name, p.price * sum(o.amount) as TOTAL_SALES
from food_product p left join food_order o on p.product_id = o.product_id
where o.produce_date like "2022-05%"
group by p.product_id
order by TOTAL_SALES desc, p.product_id asc