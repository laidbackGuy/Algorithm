-- 코드를 입력하세요
SELECT I.FOOD_TYPE, I.REST_ID, I.REST_NAME, I.FAVORITES 
FROM REST_INFO I
JOIN (SELECT FOOD_TYPE, max(FAVORITES) AS M
FROM REST_INFO
GROUP BY FOOD_TYPE) as S
ON I.FOOD_TYPE = S.FOOD_TYPE and I.FAVORITES = S.M
ORDER BY I.FOOD_TYPE DESC
