# 안녕
import sys
input = sys.stdin.readline

N = int(input())
costs = list(map(int, input().split()))
pleasures = list(map(int, input().split()))
HP = 100
dp = [[0] * 100 for _ in range(N)]

for j in range(1, 100):
    if j >= costs[0]:
        dp[0][j] = pleasures[0]

for i in range(1, N):
    for j in range(1, 100):
        cost = costs[i]
        pleasure = pleasures[i]
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + pleasure)

print(dp[N-1][99])