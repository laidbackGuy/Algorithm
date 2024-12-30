# 로봇 청소기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
si, sj, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def clean(i, j, dir):
    global answer

    while 1:
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if arr[i][j] == 0 and cleaned[i][j] == 0:
            cleaned[i][j] = 1
            answer += 1

        flag = False
        for di, dj in didj:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and cleaned[ni][nj] == 0:
                    flag = True
                    break
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        if flag:
            while 1:
                # 반시계 방향으로 90도 회전한다.
                dir -= 1
                if dir == -1:
                    dir = 3

                # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                di, dj = didj[dir]
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == 0 and cleaned[ni][nj] == 0:
                        i, j = ni, nj
                        break
                    else:
                        continue
                else:
                    continue

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        else:
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if dir == 0:
                behind = 2
            elif dir == 1:
                behind = 3
            elif dir == 2:
                behind = 0
            else:
                behind = 1

            bi, bj = didj[behind]
            ni, nj = i + bi, j + bj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    i, j = ni, nj
                    continue
                # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                else:
                    return

            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                return


didj = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 0
cleaned = [[0] * M for _ in range(N)]
clean(si, sj, d)
print(answer)