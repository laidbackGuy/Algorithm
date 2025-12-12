# 회전 초밥
import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

answer = 0
sushi_cnt = [0] * (d + 1)
cur_unique_sushi = 0

for i in range(k):
    now = sushi[i]
    if sushi_cnt[now] == 0:
        cur_unique_sushi += 1
        if sushi_cnt[c] == 0:
            answer = max(answer, cur_unique_sushi + 1)
        else:
            answer = max(answer, cur_unique_sushi)
    sushi_cnt[now] += 1

for i in range(N):
    new = sushi[(i+k) % N]
    out = sushi[i]
    if sushi_cnt[new] == 0:
        cur_unique_sushi += 1
    sushi_cnt[new] += 1
    sushi_cnt[out] -= 1
    if sushi_cnt[out] == 0:
        cur_unique_sushi -= 1
    if sushi_cnt[c] == 0:
        answer = max(answer, cur_unique_sushi + 1)
    else:
        answer = max(answer, cur_unique_sushi)

print(answer)

# set과 max 이용
# answer = 0
#
# q = deque(sushi[:k])
# my_set = set(q)
# my_set.add(c)
# answer = max(len(my_set), answer)
#
# for i in range(k, N):
#     now = sushi[i]
#     q.popleft()
#     q.append(now)
#     my_set = set(q)
#     my_set.add(c)
#     answer = max(len(my_set), answer)
#
# for i in range(k-1):
#     now = sushi[i]
#     q.popleft()
#     q.append(now)
#     my_set = set(q)
#     my_set.add(c)
#     answer = max(len(my_set), answer)
#
# print(answer)