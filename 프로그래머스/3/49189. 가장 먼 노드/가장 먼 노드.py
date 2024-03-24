from collections import deque

def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)
    
    return bfs(n, adj)

def bfs(n, adj):
    queue = deque([1])
    visited = [0] * (n+1)
    visited[1] = 1
    
    while queue:
        now = queue.popleft()
        
        for next in adj[now]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = visited[now] + 1
    # print(visited)
    answer = 0
    max_v = 0
    for i in range(1, n+1):
        if visited[i] > max_v:
            max_v = visited[i]
            answer = 1
        elif visited[i] == max_v:
            answer += 1
    return answer
        