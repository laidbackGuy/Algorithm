# 미로 탐색
def bfs():
    queue = []
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        # print('while')
        i, j = queue.pop(0)
        if (i, j) == (N-1, M-1):
            return visited[i][j]
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            # print(ni, nj)
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == '1' and visited[ni][nj] == 0:
                queue.append((ni, nj))
                # print(queue)
                visited[ni][nj] = visited[i][j] + 1


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
# print(maze)
visited = [[0] * M for _ in range(N)]
print(bfs())
# for row in visited:
#     print(row)