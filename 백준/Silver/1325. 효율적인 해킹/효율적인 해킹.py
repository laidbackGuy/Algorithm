# 효율적인 해킹
from collections import deque

def bfs(s):
    visited = [0] * (V+1)
    visited[s] = 1
    queue = deque([s])
    cnt = 1
    while queue:
        n = queue.popleft()
        for w in adj[n]:
            if visited[w] == 0:
                queue.append(w)
                cnt += 1
                visited[w] = 1
    return cnt

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for i in range(E):
    a, b = map(int, input().split())
    adj[b].append(a)

max_cnt = 0
cnt_list = [0] * (V+1)
for i in range(1, V+1):
    hack_cnt = bfs(i)
    # print(i, hack_cnt)
    if hack_cnt >= max_cnt:
        max_cnt = hack_cnt
        cnt_list[i] = max_cnt

candidates = []
for i in range(1, V+1):
    if cnt_list[i] == max_cnt:
        candidates.append(i)
print(*candidates)
