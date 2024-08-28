# 스티커
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for l in range(2):
        arr.append(list(map(int, input().split())))

    dp = [[0]*n for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n >= 2:
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]

    answer = 0
    if n > 2:
        for j in range(2, n):
            dp[0][j] = max(dp[1][j-1], dp[0][j-2], dp[1][j-2]) + arr[0][j]
            dp[1][j] = max(dp[0][j-1], dp[0][j-2], dp[1][j-2]) + arr[1][j]

            answer = max(dp[0][j], dp[1][j])
    elif n == 2:
        answer = max(arr[0][0] + arr[1][1], arr[1][0] + arr[0][1])
    else:
        answer = max(arr[0][0], arr[1][0])
    print(answer)
