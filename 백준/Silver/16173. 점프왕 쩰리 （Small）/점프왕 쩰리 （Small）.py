# 점프왕 쩰리
def bfs():
    queue = []
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        i, j = queue.pop(0)
        # print(i, j)
        if arr[i][j] == -1:
            return 'HaruHaru'
        elif arr[i][j] == 0:
            return 'Hing'
        jump_dis = arr[i][j]
        for di, dj in [[0, jump_dis], [jump_dis, 0]]:
            ni, nj = i + di, j + dj
            if ni > N - 1 or nj > N - 1:
                continue
            else:
                if visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    # print(queue)
                    visited[ni][nj] = 1
    return 'Hing'


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
print(bfs())
# print(arr)
