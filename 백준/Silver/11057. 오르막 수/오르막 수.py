# 오르막 수
import sys
input = sys.stdin.readline

N = int(input())
memo = [0] * 1001
memo[1] = 10
memo[2] = 55
prev = [i for i in range(10, 1, -1)]

for i in range(3, N+1):
    now = memo[i-1]
    temp = now
    for k in range(9):
        record = temp
        temp -= prev[k]
        now += temp
        prev[k] = record
    memo[i] = now
print(memo[N] % 10007)