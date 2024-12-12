# 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = [[]]
for _ in range(N):
    table.append(list(map(int, input().split())))

dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = table[i][0]
        value = table[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            # dp[i-1][j] : 현재 물건을 넣지 않았을 경우의 최대 가치
            # dp[i-1][j-weight] + value : 현재 물건을 넣고 남은 무게만큼 넣을 수 있는 물건들 넣은 경우의 최대 가치
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N][K])