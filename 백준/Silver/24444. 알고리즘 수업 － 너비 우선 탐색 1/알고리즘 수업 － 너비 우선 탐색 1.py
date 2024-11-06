# 알고리즘 수업 - 너비 우선 탐색 1
import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
for hi in adj:
    hi.sort()
visited = [0] * (N+1)
visited[R] = 1
q = deque([R])
cnt = 2
while q:
    now = q.popleft()
    for next in adj[now]:
        if not visited[next]:
            q.append(next)
            visited[next] = cnt
            cnt += 1

for i in range(1, N+1):
    print(visited[i])