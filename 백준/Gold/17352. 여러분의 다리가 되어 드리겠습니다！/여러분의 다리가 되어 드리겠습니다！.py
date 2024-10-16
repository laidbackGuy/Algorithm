from collections import deque

N = int(input())
if N == 2:
    print(1, 2)
else:
    adj = [[] for _ in range(N+1)]
    for _ in range(N-2):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    visited = [0] * (N+1)
    queue = deque([1])
    while queue:
        now = queue.popleft()
        for next in adj[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1
    for i in range(2, N+1):
        if not visited[i]:
            print(1, i)
            break