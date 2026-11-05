-- 코드를 입력하세요
select b.book_id, a.author_name, b.published_date
from book b left join author a on b.author_id = a.author_id
where b.category = '경제'
order by b.published_date asc