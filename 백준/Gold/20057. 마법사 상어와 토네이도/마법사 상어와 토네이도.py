# 마법사 상어와 토네이도
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def tornado(i, j, direction):
    global answer
    lst = [[-1, 0, 0.07], [-2, 0, 0.02], [-1, -1, 0.1], [-1, 1, 0.01], [0, -2, 0.05], [1, 0, 0.07], [2, 0, 0.02], [1, -1, 0.1], [1, 1, 0.01]]
    remain = arr[i][j]
    for di, dj, k in lst:
        K = int(arr[i][j] * k)
        if direction == 0:
            ni, nj = i + di, j + dj
        elif direction == 1:
            ni, nj = i - dj, j - di
        elif direction == 2:
            ni, nj = i + di, j - dj
        elif direction == 3:
            ni, nj = i + dj, j - di
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += K
        else:
            answer += K
        remain -= K
    if direction == 0:
        ni, nj = i, j - 1
    elif direction == 1:
        ni, nj = i + 1, j
    elif direction == 2:
        ni, nj = i, j + 1
    elif direction == 3:
        ni, nj = i - 1, j
    if 0 <= ni < N and 0 <= nj < N:
        arr[ni][nj] += remain
    else:
        answer += remain


didj = [[0, -1], [1, 0], [0, 1], [-1, 0]]
dir = 0
answer = 0
i, j = N // 2, N // 2
cnt = 0
limit_cnt = 0
limit = 1
while 1:
    # 이동
    i, j = i + didj[dir][0], j + didj[dir][1]
    tornado(i, j, dir)
    if i == 0 and j == 0:
        break
    # for r in arr:
    #     print(r)
    # print()
    cnt += 1
    if cnt == limit:
        cnt = 0
        dir = (dir + 1) % 4
        limit_cnt += 1
        if limit_cnt == 2:
            limit_cnt = 0
            limit += 1
print(answer)