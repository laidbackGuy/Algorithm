-- 코드를 작성해주세요
SELECT (case
       when month(DIFFERENTIATION_DATE) > 9 then '4Q'
        when month(DIFFERENTIATION_DATE) > 6 then '3Q'
        when month(DIFFERENTIATION_DATE) > 3 then '2Q'
        else '1Q'
        end) as QUARTER,
        count(*) as ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER