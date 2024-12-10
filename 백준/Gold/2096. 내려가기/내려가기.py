# 내려가기
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_dp = arr
min_dp = arr

for _ in range(1, N):
    now = list(map(int, input().split()))
    min_dp = [min(min_dp[0], min_dp[1]) + now[0], min(min_dp) + now[1], min(min_dp[1], min_dp[2]) + now[2]]
    max_dp = [max(max_dp[0], max_dp[1]) + now[0], max(max_dp) + now[1], max(max_dp[1], max_dp[2]) + now[2]]
    
a = min(min_dp)
b = max(max_dp)
print(b, a)