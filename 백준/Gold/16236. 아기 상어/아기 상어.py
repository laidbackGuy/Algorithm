# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
si, sj = None, None
fish_cnt = 0
shark_size = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si, sj = i, j
        elif arr[i][j]:
            fish_cnt += 1


def find(si, sj):
    global shark_size
    visited = [[-1] * N for _ in range(N)]
    visited[si][sj] = 0
    q = deque([(si, sj)])
    min_dis = 1e9
    flag = False
    target_fish = []
    while q:
        i, j = q.popleft()
        if flag and 0 < arr[i][j] < shark_size:
        # if flag and visited[i][j] >= min_dis:
            min_i, min_j = 20, 20
            target_idx = None
            for k in range(len(target_fish)):
                ci = target_fish[k][0]
                cj = target_fish[k][1]
                if ci < min_i:
                    min_i, min_j = ci, cj
                    target_idx = k
                    continue
                if ci == min_i:
                    if cj < min_j:
                        min_i, min_j = ci, cj
                        target_idx = k
                        continue
            return target_fish[target_idx][0], target_fish[target_idx][1], min_dis
        for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                next = arr[ni][nj]
                if visited[ni][nj] == -1 and next <= shark_size:
                    dis = visited[i][j]
                    if 0 < next < shark_size:
                        if dis + 1 < min_dis:
                            min_dis = dis + 1
                            target_fish.append((ni, nj))
                            flag = True
                        elif dis + 1 == min_dis:
                            target_fish.append((ni, nj))
                            flag = True
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return 0, 0, 0


time = 0
eat_cnt = 0
while fish_cnt > 0:
    ti, tj, spend = find(si, sj)
    if not spend:
        break
    else:
        fish_cnt -= 1
        eat_cnt += 1
        arr[ti][tj] = 9
        arr[si][sj] = 0
        if eat_cnt == shark_size:
            shark_size += 1
            eat_cnt = 0
        si, sj = ti, tj
        time += spend
print(time)