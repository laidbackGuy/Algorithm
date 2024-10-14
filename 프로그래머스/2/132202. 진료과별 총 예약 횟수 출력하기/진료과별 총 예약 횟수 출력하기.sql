-- 코드를 입력하세요
SELECT MCDP_CD as 진료과코드, count(PT_NO) as 5월예약건수 FROM APPOINTMENT
WHERE date_format(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY 진료과코드
ORDER BY 5월예약건수 ASC, 진료과코드 ASC