# 농장 관리
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


def same_height_check(si, sj, h):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    peak_candi = [(si, sj)]
    while q:
        i, j = q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0 and farm[ni][nj] == h:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    peak_candi.append((ni, nj))
    # print(si, sj)
    # for r in visited:
    #     print(r)
    # print()
    return peak_candi


def peak_check(arr, h):
    for i, j in arr:
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if farm[ni][nj] > h:
                    return False
    return True


answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            height = farm[i][j]
            peak_candi_list = same_height_check(i, j, height)
            res = peak_check(peak_candi_list, height)
            if res:
                answer += 1
            # print(height, res)
print(answer)