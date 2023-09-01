# 토마토(3차원)
import sys
from collections import deque

input = sys.stdin.readline

# 토마토_BFS
def find_ripe_tomato_empty(V):
    # 비어있는 칸의 좌표를 찾아 visited에 -1을 넣어주고
    # 익은 토마토의 좌표를 찾아 들어있는 리스트로 반환해주는 함수
    ripe_tomato_roc = []
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if tomato_arr[h][i][j] == -1:
                    V[h][i][j] = -1
                elif tomato_arr[h][i][j] == 1:
                    ripe_tomato_roc.append((h, i, j))
    return ripe_tomato_roc


def bfs(r_tomato_roc, V):
    queue = deque()                         # 큐 생성
    for roc in r_tomato_roc:                # 익은 토마토(시작점들)의 좌표를
        queue.append(roc)                   # 인큐
        r_tomato_h, r_tomato_i, r_tomato_j = roc
        visited[r_tomato_h][r_tomato_i][r_tomato_j] = 1 # visited에 1 추가(방문 처리)
    # print(queue)
    max_visited = 1                         # visited의 최댓값
    while queue:                            # 큐가 다 비워질 때까지
        h, i, j = queue.popleft()              # 디큐
        for dh, di, dj in [[0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]:   # 델타 탐색
            nh, ni, nj = h + dh, i + di, j + dj

            # 탐색 범위가 행렬을 벗어나지 않고,
            # 방문한 적이 없고.
            # 토마토가 있다면,
            # (ni, nj)를 인큐
            if 0 <= nh < H \
                    and 0 <= ni < N \
                    and 0 <= nj < M \
                    and V[nh][ni][nj] == 0 \
                    and tomato_arr[nh][ni][nj] != -1:
                queue.append((nh, ni, nj))
                V[nh][ni][nj] = V[h][i][j] + 1
                if V[nh][ni][nj] > max_visited:    # visited에 추가하는 숫자를 max_visited와 비교하며
                    max_visited = V[nh][ni][nj]     # max_visited보다 크면 max_visited에 재할당
    # print(V)
    # 너비우선탐색을 마치고 나서
    # visited 전체를 순회하여
    # 0이 있다면(익지 않은 토마토가 있다면)
    # return -1
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if V[h][i][j] == 0:
                    return -1
    # for h in range(H):
    # print(V)
    # 토마토가 전부 다 익었다면
    # max_visited에서 1을 빼서 return
    return max_visited - 1


M, N, H = map(int, input().split())
tomato_arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

# 익은 토마토들의 좌표와 토마토가 들어있지 않은 칸들을 찾는다.
ripe_tomato_roc_list = find_ripe_tomato_empty(visited)

# 너비우선탐색을 실시하여 토마토가 전부 익는 데 며칠이 걸리는지 구한다.
res = bfs(ripe_tomato_roc_list, visited)

print(res)