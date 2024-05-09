# 포도주 시식

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0] * N

dp[0] = arr[0]

if N > 1:
    dp[1] = arr[0] + arr[1]
if N > 2:
    dp[2] = max(arr[0]+arr[2], arr[1] + arr[2])
if N > 3:
    for i in range(3, N):
        dp[i] = max(dp[i-2], dp[i-3] + arr[i-1]) + arr[i]

    for i in range(3, N):
        dp[i] = max(max(dp[:i-1]), max(dp[:i-2]) + arr[i-1]) + arr[i]
# print(dp)
print(max(dp))