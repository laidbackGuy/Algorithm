# 노드 사이의 거리
def bfs(s, g):
    queue = [s]
    visited = [0] * (N+1)
    visited[s] = 1
    while queue:
        # print(queue)
        n = queue.pop(0)
        # print('n:', n)
        if n == g:
            # print(visited)
            return visited[n] - 1
        for w in range(1, N+1):
            if adj[n][w] and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[n] + adj[n][w]


N, M = map(int, input().split())
adj = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    v1, v2, dis = map(int, input().split())
    adj[v1][v2] = dis
    adj[v2][v1] = dis
# print(adj)

for _ in range(M):
    s, g = map(int, input().split())
    print(bfs(s, g))

