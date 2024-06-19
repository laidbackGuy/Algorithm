# 치즈
from collections import deque
import copy

didj = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def find_empty(i, j):
    global space
    queue = deque([(i, j)])
    if space >= 1:
        empty_visited[i][j] = 2
    else:
        empty_visited[i][j] = 1

    while queue:
        i, j = queue.popleft()
        for di, dj in didj:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and empty_visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    if space >= 1:
                        empty_visited[ni][nj] = 2
                    else:
                        empty_visited[ni][nj] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

while 1:
    # 치즈 내부에 빈 공간 있는지 알아보기
    empty_visited = [[0] * M for _ in range(N)]
    space = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and empty_visited[i][j] == 0:
                find_empty(i, j)
                space += 1

    # 치즈 녹이기
    cheese = False
    new_arr = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cheese = True
                cnt = 0
                for di, dj in didj:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 0 and empty_visited[ni][nj] != 2:
                            cnt += 1
                            if cnt == 2:
                                new_arr[i][j] = 0
                                break

    # 치즈가 전부 녹았나 체크
    if cheese is False:
        break

    arr = new_arr
    answer += 1

print(answer)