# 욕심쟁이 판다
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
didj = [[-1, 0], [0, -1], [1, 0], [0, 1]]
memo = [[0] * N for _ in range(N)]


def check(i, j):
    global answer
    temp = 1
    for di, dj in didj:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] > arr[i][j]:
                if memo[ni][nj]:
                    temp = max(temp, memo[ni][nj] + 1)
                else:
                    temp = max(temp, check(ni, nj) + 1)
    memo[i][j] = temp
    return memo[i][j]


answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, check(i, j))
print(answer)