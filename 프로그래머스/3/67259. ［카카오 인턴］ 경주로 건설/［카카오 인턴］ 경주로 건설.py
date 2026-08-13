from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    INF = 1e9
    dp = [[INF] * n for _ in range(n)]
    dp_r = [[INF] * n for _ in range(n)]
    dp[0][0] = 0
    dp_r[n-1][n-1] = 0
    didj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    # for r in board:
    #     print(r)
    # print()
    
    def bfs():
        
        q = deque([])
        
        if board[0][1] == 0:
            q.append((0, 1, 100, 1))
            dp[0][1] = 100
        if board[1][0] == 0:
            q.append((1, 0, 100, 0))
            dp[1][0] = 100
            
        while q:
            i, j, cost, pre_dir = q.popleft()
            for d in range(4):
                ni, nj = i + didj[d][0], j + didj[d][1]
                if 0 <= ni < n and 0 <= nj < n:
                    if pre_dir == d:
                        new_cost = 100
                    else:
                        new_cost = 600
                    if cost + new_cost <= dp[ni][nj] and board[ni][nj] == 0:
                        q.append((ni, nj, cost + new_cost, d))
                        dp[ni][nj] = cost + new_cost
    
    
    def bfs_r():
        q = deque([])

        if board[n-1][n-2] == 0:
            q.append((n-1, n-2, 100, 3))
            dp_r[n-1][n-2] = 100
        if board[n-2][n-1] == 0:
            q.append((n-2, n-1, 100, 2))
            dp_r[n-2][n-1] = 100
            
        while q:
            i, j, cost, pre_dir = q.popleft()
            for d in range(4):
                ni, nj = i + didj[d][0], j + didj[d][1]
                if 0 <= ni < n and 0 <= nj < n:
                    if pre_dir == d:
                        new_cost = 100
                    else:
                        new_cost = 600
                    if cost + new_cost <= dp_r[ni][nj] and board[ni][nj] == 0:
                        q.append((ni, nj, cost + new_cost, d))
                        dp_r[ni][nj] = cost + new_cost
    
    
    bfs()
    bfs_r()
    
    # for r in dp:
    #     print(r)
    # print()
    # for r in dp_r:
    #     print(r)
                         
    return min(dp[n-1][n-1], dp_r[0][0])