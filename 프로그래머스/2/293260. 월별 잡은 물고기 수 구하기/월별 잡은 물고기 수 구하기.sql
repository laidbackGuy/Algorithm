-- 코드를 작성해주세요
SELECT count(*) as FISH_COUNT, month(TIME) as MONTH from FISH_INFO
GROUP BY MONTH
HAVING FISH_COUNT > 0
ORDER BY MONTH