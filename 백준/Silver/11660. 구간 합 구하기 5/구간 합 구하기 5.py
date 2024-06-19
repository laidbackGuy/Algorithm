# 구간 합 구하기 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
cur = 0
for i in range(N):
    cur = 0
    for j in range(N):
        cur += arr[i][j]
        dp[i][j] = cur

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    for i in range(x1-1, x2):
        if y1 > 1:
            answer += dp[i][y2-1] - dp[i][y1-2]
        else:
            answer += dp[i][y2 - 1]

    print(answer)
