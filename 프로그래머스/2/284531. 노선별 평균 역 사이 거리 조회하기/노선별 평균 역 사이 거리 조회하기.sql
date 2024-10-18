-- 코드를 작성해주세요
select ROUTE, concat(round(sum(d_between_dist), 1), 'km') as TOTAL_DISTANCE, concat(round(avg(d_between_dist), 2), 'km') as AVERAGE_DISTANCE from subway_distance
group by route
order by sum(d_between_dist) desc
# ORDER BY TOTAL_DISTANCE 로 했다가 틀렸는데,
# TOTAL_DISTANCE는 소수점 반올림으로 한 번 가공한 데이터이기 때문에 
# TOTAL_DISTANCE를 기준으로 정렬하면 안되는 것임.