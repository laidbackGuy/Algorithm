from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    
    def bfs(s):
        q = deque([s])
        
        while q:
            now = q.popleft()
            for next in range(n):
                if visited[next] == 0 and computers[now][next] == 1:
                    q.append(next)
                    visited[next] = 1
        
        
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer