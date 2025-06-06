# N-Queen
import sys
input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]
check = [[0] * N for _ in range(N)]
answer = 0
'''
1. 첫째 줄에 차례대로 퀸을 1개 놓는다
2. 퀸을 1개 놓을 때마다 그 아랫줄들에 공격할 수 있는 칸들 모두 check 각 칸에 1씩 더해줌
3. 다음 줄 넘어와서 놓을 수 있는 칸(check배열에서 0인 칸)에 퀸 1개 놓기
4. 만약 현재 줄에서 놓을 수 있는 칸이 없다면 False
5. 마지막 줄까지 와서 퀸을 1개씩 다 놓았다면 True
6. 공격 가능한 칸들 체크는, check 배열에 각 칸별로 cnt를 쌓는 방식으로.
7. 재귀 방식으로 한줄씩 타고 내려가면서, 불가능하면 윗줄로 돌아감.
8. 윗줄로 돌아갈 때 윗줄의 이전에 놨던 퀸이 공격할 수 있는 칸들 check각 칸에서 다시 1씩 빼줌.
'''


def attack_check(i, j, temp):
    if temp == 'check':
        for di, dj in [[1, 0], [1, -1], [1, 1]]:    # 아래 3방향으로만 체크
            for k in range(1, N):
                ni, nj = i + di*k, j + dj*k
                if 0 <= ni < N and 0 <= nj < N:
                    check[ni][nj] += 1
    elif temp == 'erase':
        for di, dj in [[1, 0], [1, -1], [1, 1]]:    # 아래 3방향으로만 체크
            for k in range(1, N):
                ni, nj = i + di*k, j + dj*k
                if 0 <= ni < N and 0 <= nj < N:
                    check[ni][nj] -= 1


def n_queen(floor):
    global answer

    for j in range(N):
        if check[floor][j] == 0:
            if floor == N-1:
                # board[floor][j] = 'Q'
                # for r in board:
                #     print(r)
                # board[floor][j] = 0
                # print()
                answer += 1
                continue
            board[floor][j] = 'Q'
            attack_check(floor, j, 'check')
            n_queen(floor + 1)
            board[floor][j] = 0
            attack_check(floor, j, 'erase')


n_queen(0)
print(answer)