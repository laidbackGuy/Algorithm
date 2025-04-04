-- 코드를 작성해주세요
SELECT e.DEPT_ID, d.DEPT_NAME_EN, ROUND(avg(e.SAL), 0) as AVG_SAL
FROM HR_EMPLOYEES e
JOIN HR_DEPARTMENT d on e.DEPT_ID = d.DEPT_ID
GROUP BY e.DEPT_ID
ORDER BY AVG_SAL DESC