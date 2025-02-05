# Project Teams
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 1e9
for i in range(n):
    now = arr[i] + arr[-(i+1)]
    answer = min(answer, now)
print(answer)