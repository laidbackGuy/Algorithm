# 정수 삼각형

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = []
for i in range(n):
    dp.append([0]*(i+1))

dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[n-1]))