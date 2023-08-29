# 헌내기는 친구가 필요해

def find_friends(si, sj):
    global visited
    global cnt
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1

    while queue:
        i, j = queue.pop(0)
        if campus[i][j] == 'P':
            cnt += 1
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and campus[ni][nj] != 'X' and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1


N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0

# 도연이 좌표 찾기
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            find_friends(i, j)
if cnt == 0:
    cnt = 'TT'
print(cnt)
