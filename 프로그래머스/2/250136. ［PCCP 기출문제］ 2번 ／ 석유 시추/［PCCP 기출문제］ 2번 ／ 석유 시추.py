from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    
    visited = [[0] * m for _ in range(n)]
    
    
    def bfs(si, sj):
        q = deque([(si, sj)])
        visited[si][sj] = 1
        size = 1
        min_j, max_j = sj, sj
        
        while q:
            i, j = q.popleft()
            for di, dj in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if land[ni][nj] == 1 and visited[ni][nj] == 0:
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                        size += 1
                        if nj > max_j:
                            max_j = nj
                        elif nj < min_j:
                            min_j = nj
        return size, min_j, max_j
    
    cnt_list = [0] * m
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                size, min_j, max_j = bfs(i, j)
                for k in range(min_j, max_j + 1):
                    cnt_list[k] += size
                    
    answer = max(cnt_list)
    
        
    return answer