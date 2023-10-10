# 빙산
from collections import deque


def bfs(si, sj):
    queue = deque([(si, sj)])
    visited[si][sj] = 1
    while queue:
        # print(queue)
        ci, cj = queue.popleft()
        # print((ci, cj))
        for delta_i, delta_j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            next_i, next_j = ci + delta_i, cj + delta_j
            if 0 <= next_i < N and 0 <= next_j < M and arr[next_i][next_j] and visited[next_i][next_j] == 0:
                queue.append((next_i, next_j))
                # print(next_i, next_j)
                visited[next_i][next_j] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

year = 0
while True:
    # 내년의 빙산 상태
    next_arr = [[0] * M for _ in range(N)]
    year += 1   # 1년이 지날때마다 +1
    # 빙산 녹이기
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt = 0
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        cnt += 1
                next_num = arr[i][j] - cnt
                if next_num < 0:
                    next_num = 0
                next_arr[i][j] = next_num
    arr = next_arr

    num_ice = 0
    visited = [[0] * M for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] and visited[i][j] == 0:
                bfs(i, j)
                num_ice += 1
                flag = True

    if num_ice >= 2:
        break

    if flag is False:
        year = 0
        break


print(year)