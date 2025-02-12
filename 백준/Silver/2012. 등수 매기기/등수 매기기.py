# 등수 매기기
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
prize = 1
answer = 0
for i in range(N):
    if arr[i] != prize:
        answer += abs(prize - arr[i])
    prize += 1
print(answer)
