# 1, 2, 3 더하기 4
import sys
input = sys.stdin.readline

dp = [0] * 10001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 5
dp[6] = 7
dp[7] = 8
dp[8] = 10
dp[9] = 12
dp[10] = 14

arr = [0, 1, 0, 1, 1, 1]
T = int(input())
for _ in range(T):
    n = int(input())
    if n > 10:
        temp = 0
        add = 2
        for i in range(11, n+1):
            # print(i, arr[temp], add)
            dp[i] = dp[i-1] + arr[temp] + add
            temp += 1
            if temp == 6:
                add += 1
                temp = 0
        print(dp[n])
    else:
        print(dp[n])