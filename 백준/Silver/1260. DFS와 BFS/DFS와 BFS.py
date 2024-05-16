# BFS와 DFS

def dfs(s, adj):
    res = []
    stack = []
    visited = [0] * (V+1)

    n = s                   # n에 시작점 할당
    visited[n] = 1          # 방문표시
    res.append(n)
    while True:
        adj[n].sort()               # 인접 리스트에서 연결된 점들 오름차순 정렬
        for w in adj[n]:            # 연결된 점들 중
            if visited[w] == 0:     # 방문 안 한 점이 있으면
                stack.append(n)     # 기존 점 스택에 push하고
                n = w               # 정점 w 방문
                visited[n] = 1      # 방문 표시
                res.append(n)
                break
        else:                       # 갈 정점 없다면
            if stack:               # 스택에 뭐가 들어있으면
                n = stack.pop()     # 가장 최근에 넣어놓은 점으로 돌아가
            else:                   # 스택 비었으면
                break               # 탐색 끝
    return res


def bfs(s, adj):
    res = []
    visited = [0] * (V+1)
    queue = []

    queue.append(s)                 # 시작점 인큐
    visited[s] = 1                  # 방문 표시
    res.append(s)
    while queue:                    # 큐가 비워질 때까지 반복
        t = queue.pop(0)            # 큐에 제일 먼저 넣었던 정점 디큐(t)
        for w in adj[t]:            # t에서 연결된 정점들 중
            if visited[w] == 0:     # 방문 안 한 정점 있으면
                queue.append(w)     # 인큐
                visited[w] = 1      # 방문 표시
                res.append(w)
    return res

V, E, start = map(int, input().split())
adj_l = [[] for _ in range(V+1)]

for i in range(E):
    A, B = map(int, input().split())
    adj_l[A].append(B)
    adj_l[B].append(A)
# print(adj_l)
res = dfs(start, adj_l)
print(*res)
res = bfs(start, adj_l)
print(*res)

