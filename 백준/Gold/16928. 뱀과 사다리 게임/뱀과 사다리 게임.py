# 뱀과 사다리 게임 solving
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(107)]
for i in range(1, 107):
    for k in range(1, 7):
        adj[i].append(i+k)
adj_ladder_snake = [[] for _ in range(107)]
for _ in range(N):
    x, y = map(int, input().split())
    adj_ladder_snake[x].append(y)
for _ in range(M):
    u, v = map(int, input().split())
    adj_ladder_snake[u].append(v)

visited = [0] * 107
queue = deque([1])
while queue:
    now = queue.popleft()
    if now == 100:
        break
    dist = visited[now]
    if adj_ladder_snake[now]:
        now = adj_ladder_snake[now][0]
    for next in adj[now]:
        if visited[next] == 0:
            queue.append(next)
            visited[next] = dist + 1
print(visited[100])