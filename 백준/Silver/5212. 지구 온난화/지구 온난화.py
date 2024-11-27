# 지구 온난화
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

min_i, min_j = N, M
max_i, max_j = 0, 0

new_arr = [['.'] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            cnt = 0
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt == 3 or cnt == 4:
                continue
            else:
                new_arr[i][j] = 'X'
                min_i = min(min_i, i)
                max_i = max(max_i, i)
                min_j = min(min_j, j)
                max_j = max(max_j, j)

for i in range(min_i, max_i+1):
    print(''.join(new_arr[i][min_j:max_j+1]))
