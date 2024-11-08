# 합이 0인 네 정수
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    now = list(map(int, input().split()))
    A.append(now[0])
    B.append(now[1])
    C.append(now[2])
    D.append(now[3])

answer = 0
ab_dict = defaultdict(int)
for i in range(N):
    for j in range(N):
        ab_dict[A[i] + B[j]] += 1
for i in range(N):
    for j in range(N):
        now = C[i] + D[j]
        if -now in ab_dict.keys():
            answer += ab_dict[-now]
print(answer)