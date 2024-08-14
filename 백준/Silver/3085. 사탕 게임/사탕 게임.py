# 사탕 게임
def check_max_eat(arr, n):
    # 같은 색상의 사탕 최대 길이 구해주는 함수
    max_eat = 1
    # 행 순회
    for i in range(n):
        cnt = 1
        for j in range(n):
            if j+1 < n:
                if arr[i][j] == arr[i][j+1]:
                    cnt += 1
                    if cnt > max_eat:
                        max_eat = cnt
                else:
                    cnt = 1
    # 열 순회
    for j in range(n):
        cnt = 1
        for i in range(n):
            if i+1 < n:
                if arr[i][j] == arr[i+1][j]:
                    cnt += 1
                    if cnt > max_eat:
                        max_eat = cnt
                else:
                    cnt = 1
    return max_eat

N = int(input())
board = [list(input()) for _ in range(N)]
# print(board)

res_max_eat = check_max_eat(board, N)
# 행, 열 순회하며 오른쪽, 아래 방향 바꿔가며 확인
for i in range(N):
    for j in range(N):
        for di, dj in [[1, 0], [0, 1]]:     # 오른쪽, 아래쪽 방향 살펴보기
            ni, nj = i + di, j + dj
            if ni < N and nj < N:
                if board[i][j] != board[ni][nj]:    # 인접한 사탕과 색이 다르다면
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]     # 자리 바꿔주기
                    max_eat = check_max_eat(board, N)   # 같은 색 최대 길이 세어주고
                    if max_eat > res_max_eat:       # 전체에서 최대 길이 찾기
                        res_max_eat = max_eat
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]     # 자리 원상복귀

print(res_max_eat)

