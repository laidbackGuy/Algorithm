# 진우의 달 여행 (small)
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.append([0] * M)
res = 1e9
dp = [[1e9] * M for _ in range(N)]


def bfs(sj, dist):
    global res
    q = deque([(0, sj, dist, 2)])
    while q:
        i, j, cur, prev = q.popleft()

        # print(i, j, cur, prev)
        if i == N:
            res = min(res, cur)
            continue
        if cur < dp[i][j]:
            dp[i][j] = cur
        if j == 0:
            if prev == 0:
                next = [1]
            else:
                next = [0, 1]
            for k in next:
                q.append((i+1, j+k, cur + arr[i+1][j+k], k))
        elif j == M-1:
            if prev == 0:
                next = [-1]
            else:
                next = [-1, 0]
            for k in next:
                q.append((i+1, j+k, cur + arr[i+1][j+k], k))
        else:
            next = [-1, 0, 1]
            if prev == 0:
                next = [-1, 1]
            elif prev == -1:
                next = [0, 1]
            elif prev == 1:
                next = [-1, 0]
            for k in next:
                q.append((i+1, j+k, cur + arr[i+1][j+k], k))


for j in range(M):
    bfs(j, arr[0][j])
    # print('asdasdasdasdasdasdasdasdasdasd')
print(res)

# for r in dp:
#     print(r)

# 연속 같은 방향 안돼서 뒤에까지 가봐야 최솟값의 경로를 알 수 있음.
# dp = [[0] * M for _ in range(N)]
# prev_j = [[-2] * M for _ in range(N)]
# for j in range(M):
#     dp[0][j] = arr[0][j]
#
# for i in range(1, N):
#     # 맨 왼쪽
#     candis = []
#     if prev_j[i-1][0] != 0:
#         candis.append(0)
#     if prev_j[i-1][1] != 1:
#         candis.append(1)
#     min_cost = 1e9
#     now_dir = None
#     flag = False
#     for k in candis:
#         if dp[i-1][k] < min_cost:
#             min_cost = dp[i-1][k]
#             now_dir = k
#         elif dp[i-1][k] == min_cost:
#             flag = True
#     dp[i][0] = min_cost + arr[i][0]
#     if flag:
#         prev_j[i][0] = 2
#     else:
#         prev_j[i][0] = now_dir
#
#     # 맨 오른쪽
#     candis = []
#     if prev_j[i - 1][M-1] != 0:
#         candis.append(0)
#     if prev_j[i - 1][M-2] != -1:
#         candis.append(-1)
#     min_cost = 1e9
#     now_dir = None
#     flag = False
#     for k in candis:
#         if dp[i - 1][M - 1 + k] < min_cost:
#             min_cost = dp[i - 1][M - 1 + k]
#             now_dir = k
#         elif dp[i-1][M - 1 + k] == min_cost:
#             flag = True
#     dp[i][M-1] = min_cost + arr[i][M-1]
#     if flag:
#         prev_j[i][M - 1] = 2
#     else:
#         prev_j[i][M-1] = now_dir
#
#     # 중간
#     for j in range(1, M-1):
#         candis = []
#         if prev_j[i-1][j-1] != -1:
#             candis.append(-1)
#         if prev_j[i - 1][j] != 0:
#             candis.append(0)
#         if prev_j[i-1][j+1] != 1:
#             candis.append(1)
#         min_cost = 1e9
#         now_dir = None
#         flag = False
#         for k in candis:
#             if dp[i - 1][j + k] < min_cost:
#                 min_cost = dp[i - 1][j + k]
#                 now_dir = k
#             elif dp[i - 1][j + k] == min_cost:
#                 flag = True
#         dp[i][j] = min_cost + arr[i][j]
#         if flag:
#             prev_j[i][j] = 2
#         else:
#             prev_j[i][j] = now_dir
# print(min(dp[N-1]))

