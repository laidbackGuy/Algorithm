# 적록색약
def count_R(si, sj):
    queue = []
    queue.append((si, sj))
    visitied_R[si][sj] = 1
    while queue:
        i, j = queue.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'R' and visitied_R[ni][nj] == 0:
                queue.append((ni, nj))
                visitied_R[ni][nj] = 1


def count_G(si, sj):
    queue = []
    queue.append((si, sj))
    visitied_G[si][sj] = 1
    while queue:
        i, j = queue.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'G' and visitied_G[ni][nj] == 0:
                queue.append((ni, nj))
                visitied_G[ni][nj] = 1


def count_B(si, sj):
    queue = []
    queue.append((si, sj))
    visitied_B[si][sj] = 1
    while queue:
        i, j = queue.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'B' and visitied_B[ni][nj] == 0:
                queue.append((ni, nj))
                visitied_B[ni][nj] = 1


def count_RG(si, sj):
    queue = []
    queue.append((si, sj))
    visitied_RG[si][sj] = 1
    while queue:
        i, j = queue.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] == 'R' or arr[ni][nj] == 'G') and visitied_RG[ni][nj] == 0:
                queue.append((ni, nj))
                visitied_RG[ni][nj] = 1


N = int(input())
arr = [input() for _ in range(N)]

visitied_R = [[0] * N for _ in range(N)]
visitied_G = [[0] * N for _ in range(N)]
visitied_B = [[0] * N for _ in range(N)]
visitied_RG = [[0] * N for _ in range(N)]

cnt_R = 0
cnt_G = 0
cnt_B = 0
cnt_RG = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            if visitied_R[i][j] == 0:
                count_R(i, j)
                cnt_R += 1
            if visitied_RG[i][j] == 0:
                count_RG(i, j)
                cnt_RG += 1
        if arr[i][j] == 'G':
            if visitied_G[i][j] == 0:
                count_G(i, j)
                cnt_G += 1
            if visitied_RG[i][j] == 0:
                count_RG(i, j)
                cnt_RG += 1
        elif arr[i][j] == 'B' and visitied_B[i][j] == 0:
            count_B(i, j)
            cnt_B += 1
print(cnt_R + cnt_G + cnt_B, cnt_RG + cnt_B)