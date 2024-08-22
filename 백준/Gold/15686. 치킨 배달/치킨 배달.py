# 치킨 배달
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

homes = []
bhc = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            bhc.append((i, j))

candis = list(combinations(bhc, M))
answer = 1e9

for case in candis:
    case_chicken_dis = 0
    for hi, hj in homes:
        chicken_dis = 1e9
        for ci, cj in case:
            dis = abs(ci - hi) + abs(cj - hj)
            chicken_dis = min(chicken_dis, dis)
        case_chicken_dis += chicken_dis
    answer = min(answer, case_chicken_dis)

print(answer)