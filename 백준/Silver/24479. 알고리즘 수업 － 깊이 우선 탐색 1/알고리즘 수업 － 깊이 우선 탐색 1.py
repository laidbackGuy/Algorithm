# 알고리즘 수업 - 깊이 우선 탐색 1

import sys
sys.setrecursionlimit(100000)
from collections import deque

def dfs(n):
    global cnt
    if cnt == V:
        return
    visited[n] = cnt
    for w in adj_l[n]:
        if visited[w] == 0:
            cnt += 1
            visited[w] = cnt
            dfs(w)


input = sys.stdin.readline

V, E, start = map(int, input().split())
adj_l = [[] * (V+1) for _ in range(V+1)]

for i in range(E):
    A, B = map(int, input().split())
    adj_l[A].append(B)
    adj_l[B].append(A)

for row in adj_l:
    row.sort()

cnt = 1
visited = [0] * (V+1)
dfs(start)

# print(adj_l)
# print(visited)
for i in range(1, V+1):
    print(visited[i])






# stack = deque()
# visited = [0] * (V+1)
# n = start
# cnt = 1
# visited[n] = cnt
# while True:
#     for w in adj_l[n]:
#         if visited[w] == 0:
#             stack.append(n)
#             cnt += 1
#             visited[w] = cnt
#             n = w
#             # print('방문', n)
#             break
#     else:
#         if stack:
#             n = stack.pop()
#         else:
#             break
# print(adj_l)
# print(visited)
# for i in range(1, V+1):
#     print(visited[i])
