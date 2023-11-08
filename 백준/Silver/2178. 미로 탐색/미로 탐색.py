# 미로 탐색
def bfs():
    queue = [(0, 0)]
    visited[0][0] = 1
    while queue:
        i, j = queue.pop(0)
        # print(i, j)
        if i == N-1 and j == M-1:
            # for row in visited:
                # print(row)
            return visited[i][j]
        for di, dj in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '1' and not visited[ni][nj]:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
# print(arr)
visited = [[0 for _ in range(M)]for _ in range(N)]
# print(visited)
print(bfs())