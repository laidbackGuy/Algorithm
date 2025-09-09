# 빌런 호석
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
'''
"1층부터 N층까지 모든 층을 하나씩 확인하면서, "
"현재 층 X에서 해당 층으로 바꾸는 데 필요한 LED 반전 개수가 P개 이하인지 검사한다."
'''
N, K, P, X = map(int, input().split())

# arr[0][1]은 0에서 1로 바꿀 때 드는 비용
arr = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2], [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]

answer = 0
target = str(X).zfill(K)
for floor in range(1, N+1):
    res = 0
    now_floor_str = str(floor).zfill(K)
    n = len(now_floor_str)
    for i in range(n):
        res += arr[int(now_floor_str[i])][int(target[i])]
    if res <= P:
        answer += 1
print(answer-1)