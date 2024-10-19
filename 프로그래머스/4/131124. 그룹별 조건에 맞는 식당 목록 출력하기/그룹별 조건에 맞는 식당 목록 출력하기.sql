SELECT P.MEMBER_NAME, R.REVIEW_TEXT, date_format(R.REVIEW_DATE, '%Y-%m-%d')
FROM MEMBER_PROFILE P left join REST_REVIEW R on R.MEMBER_ID = P.MEMBER_ID
WHERE P.MEMBER_ID = (SELECT MEMBER_ID from REST_REVIEW
GROUP BY MEMBER_ID
ORDER BY count(*) DESC
LIMIT 1)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT