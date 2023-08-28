# 쉬운 최단 거리
def bfs(si, sj):
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 0
    while queue:
        # print('while')
        i, j = queue.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            # print(ni, nj)
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                # print(queue)
                visited[ni][nj] = visited[i][j] + 1


def find_start():
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 2:
                return i, j


N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
# print(maze)
visited = [[0] * M for _ in range(N)]

# visited에 벽 좌표를 -1로 넣어주기
for i in range(N):
    for j in range(M):
        if maze[i][j] == 0:
            visited[i][j] = -2
# 목표지점 2 찾기
si, sj = find_start()
# 거리 재기
bfs(si, sj)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            visited[i][j] = -1
        elif visited[i][j] == -2:
            visited[i][j] = 0
visited[si][sj] = 0
for row in visited:
    print(*row)