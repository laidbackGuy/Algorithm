# 회전 초밥
import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

answer = 0

q = deque(sushi[:k])
my_set = set(q)
my_set.add(c)
answer = max(len(my_set), answer)

for i in range(k, N):
    now = sushi[i]
    q.popleft()
    q.append(now)
    my_set = set(q)
    my_set.add(c)
    answer = max(len(my_set), answer)

for i in range(k-1):
    now = sushi[i]
    q.popleft()
    q.append(now)
    my_set = set(q)
    my_set.add(c)
    answer = max(len(my_set), answer)

print(answer)