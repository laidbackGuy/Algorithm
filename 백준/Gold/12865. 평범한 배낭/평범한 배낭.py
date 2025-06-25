import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = [[]]
for _ in range(N):
    table.append(list(map(int, input().split())))

dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    now_w, now_v = table[i]
    for j in range(1, K+1):
        if now_w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-now_w] + now_v)

        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])