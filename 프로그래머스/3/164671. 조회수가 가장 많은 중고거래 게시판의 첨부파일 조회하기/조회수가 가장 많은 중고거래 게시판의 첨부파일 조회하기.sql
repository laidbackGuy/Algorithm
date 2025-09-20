-- 코드를 입력하세요
SELECT concat('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
FROM USED_GOODS_FILE 
WHERE BOARD_ID in
(select BOARD_ID
from USED_GOODS_BOARD
where views =
(SELECT views
FROM USED_GOODS_BOARD 
order by views desc
limit 1))
ORDER BY FILE_ID DESC