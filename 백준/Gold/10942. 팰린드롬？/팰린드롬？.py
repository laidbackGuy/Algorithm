# 팰린드롬?
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp = [[0]*N for _ in range(N)]

for length in range(N):
    for start in range(N - length):
        end = start + length
        if start == end:
            dp[start][end] = 1
        elif nums[start] == nums[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1


for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])

