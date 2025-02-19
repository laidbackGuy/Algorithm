# 이동하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]

for i in range(1, N):
    dp[i][0] = maze[i][0] + dp[i - 1][0]
for j in range(1, M):
    dp[0][j] = maze[0][j] + dp[0][j-1]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i][j]

print(dp[N-1][M-1])
