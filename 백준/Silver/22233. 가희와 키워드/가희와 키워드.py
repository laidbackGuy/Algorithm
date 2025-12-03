# 가희와 키워드
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = {}
for _ in range(N):
    memo[input().rstrip()] = 0
post = [input().rstrip() for _ in range(M)]

answer = N

for i in range(M):
    now = list(post[i].split(','))
    for keyword in now:
        if keyword in memo:
            if memo[keyword] > 0:
                continue
            else:
                memo[keyword] = 1
                answer -= 1
    print(answer)
