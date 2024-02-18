ans = 10000
def solution(maps):
    global ans
    N = len(maps[0])
    M = len(maps)
    visited = [[0] * N for _ in range(M)]
    
    def bfs(n, m):
        global ans
        queue = [(0, 0)]
        visited[0][0] = 1
        
        while queue:
            i, j = queue.pop(0)
            if i == (m-1) and j == (n-1):
                return visited[i][j]
            for di, dj in [[1, 0], [0, 1],[ -1, 0], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if maps[ni][nj] == 1 and visited[ni][nj] == 0:
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append((ni, nj))                
        return -1
    ans = bfs(N, M)
    return ans