# 연구소
import sys, copy, itertools, collections
input = sys.stdin.readline

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

viruses = []
walls = []
blanks = []
num_blanks = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            viruses.append((i, j))
        elif arr[i][j] == 1:
            walls.append((i, j))
        else:
            blanks.append((i, j))
            num_blanks += 1

new_walls_candis = list(itertools.combinations(blanks, 3))

# 모든 벽 후보군들에 대해 브루트포스
for new_walls in new_walls_candis:
    cur_arr = copy.deepcopy(arr)
    visited = [[0] * M for _ in range(N)]

    # 벽 세우기
    for i, j in new_walls:
        cur_arr[i][j] = 1

    remain_blank = num_blanks - 3

    # 모든 바이러스 좌표에서 방문 가능한 곳 방문(BFS)
    for i, j in viruses:
        queue = collections.deque([(i, j)])

        while queue:
            i, j = queue.popleft()

            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if cur_arr[ni][nj] == 0:
                        queue.append((ni, nj))
                        cur_arr[ni][nj] = 2
                        remain_blank -= 1

    answer = max(remain_blank, answer)

print(answer)

