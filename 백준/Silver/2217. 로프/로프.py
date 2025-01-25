# 로프
import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))
num_list.sort()
answer = num_list[0] * N
remain = N - 1
for i in range(1, N):
    answer = max(answer, num_list[i] * remain)
    remain -= 1
print(answer)