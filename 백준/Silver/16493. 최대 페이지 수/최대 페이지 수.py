# 최대 페이지 수
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[]]
for _ in range(M):
    table.append(list(map(int, input().split())))
dp = [[0] * (N+1) for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        cost = table[i][0]
        page = table[i][1]
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + page)
# for r in dp:
#     print(r)
print(dp[M][N])