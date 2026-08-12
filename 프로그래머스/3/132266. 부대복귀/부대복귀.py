from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    adj = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
    
    def bfs():
        q = deque([destination])
        visited[destination] = 0
        
        while q:
            now = q.popleft()
            
            for next in adj[now]:
                if visited[next] == -1:
                    q.append(next)
                    visited[next] = visited[now] + 1
    
    
    bfs()
    
    for s in sources:
        answer.append(visited[s])
    return answer