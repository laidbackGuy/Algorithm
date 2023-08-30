# 연결 요소의 개수
import sys
input = sys.stdin.readline

def dfs(s):
    stack = []
    visited[s] = 1
    while True:
        for w in range(1, V+1):
            if adj[s][w] == 1 and visited[w] == 0:
                stack.append(s)
                s = w
                visited[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1
# print(adj)

visited = [0] * (V+1)
cnt = 0

for node in range(1, V+1):
    if visited[node] == 0:
        dfs(node)
        cnt += 1
print(cnt)