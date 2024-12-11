# 벽 부수고 이동하기 4
import sys, copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
answer = copy.deepcopy(arr)

didj = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def count_space(i, j, num):
    visited[i][j] = 1
    queue = deque([(i, j)])
    cnt = 1
    arr[i][j] = num
    while queue:
        i, j = queue.popleft()
        for di, dj in didj:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '0' and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    arr[ni][nj] = num
                    cnt += 1
                    visited[ni][nj] = 1
    return cnt


my_dict = {}
visited = [[0] * M for _ in range(N)]
number = 1
for k in range(N):
    for l in range(M):
        if arr[k][l] == '0':
            my_dict[number] = count_space(k, l, number)
            number += 1

for k in range(N):
    for l in range(M):
        if arr[k][l] == '1':
            now = 1
            plus = set()
            for di, dj in didj:
                ni, nj = k + di, l + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] != '1' and arr[ni][nj] != '0':
                        plus.add(arr[ni][nj])
            for p in plus:
                now += my_dict[p]
            answer[k][l] = str(now % 10)
for r in answer:
    print(''.join(r))
