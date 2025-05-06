# 인구 이동
import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(si, sj, spop, num):
    global flag
    q = deque([(si, sj, spop)])
    visited[si][sj] = num
    united_cnt[num] += 1
    united_pop[num] += spop

    while q:
        i, j, pop = q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj]:
                    next_pop = arr[ni][nj]
                    if L <= abs(pop - next_pop) <= R:
                        q.append((ni, nj, next_pop))
                        visited[ni][nj] = num
                        united_cnt[num] += 1
                        if united_cnt[num] >= 2:
                            flag = True
                        united_pop[num] += next_pop


day = 0
while 1:
    # for r in arr:
    #     print(r)
    temp = 1
    united_cnt = [0] * (N**2 + 1)
    united_pop = [0] * (N**2 + 1)
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, arr[i][j], temp)
                temp += 1
    # print()
    # for r in visited:
    #     print(r)
    # print()
    # print(united_cnt)
    # print(united_pop)
    # print(flag)
    # print()
    # print()
    if not flag:
        break
    else:
        # 인구 이동
        for k in range(N**2 + 1):
            uni_cnt = united_cnt[k]
            if uni_cnt >= 2:
                # print('연합:', k)
                uni_pop = united_pop[k] // uni_cnt
                # print('연합인구:', uni_pop)
                for i in range(N):
                    for j in range(N):
                        if visited[i][j] == k:
                            arr[i][j] = uni_pop
        day += 1
print(day)