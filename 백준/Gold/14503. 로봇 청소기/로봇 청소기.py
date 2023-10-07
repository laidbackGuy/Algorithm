# 로봇 청소기
di_dj_list = [
    [[-1, 0], [0, -1], [1, 0], [0, 1]],
    [[0, 1], [-1, 0], [0, -1], [1, 0]],
    [[1, 0], [0, 1], [-1, 0], [0, -1]],
    [[0, -1], [1, 0], [0, 1], [-1, 0]]
]
direction_di_dj = [[-1, 0], [0, 1], [1, 0], [0, -1]]
back_list = [[1, 0], [0, -1], [-1, 0], [0, 1]]


def clean(i, j):
    global direction
    cnt = 0    # 청소 횟수
    while True:
        flag = False
        if arr[i][j] == 0:
            arr[i][j] = 2
            cnt += 1

        # di_dj = di_dj_list[direction]

        # 주변 4칸 중 청소되지 않은 칸이 있는지 확인
        flag = False
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                flag = True     # 주변 4칸 중 청소되지 않은 칸이 있다면 flag = True
                break

        if flag is True:
            while True:
                direction -= 1
                if direction == -1:
                    direction = 3
                di, dj = direction_di_dj[direction]
                ni, nj = i + di, j + dj
                if arr[ni][nj] == 0:
                    i, j = ni, nj
                    break

        # 주변 4칸 중 청소할 칸이 없는 경우 뒤로 후진
        else:
            di, dj = back_list[direction]
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
                i, j = ni, nj
            else:
                return cnt

        # for row in arr:
        #     print(row)


N, M = map(int, input().split())
si, sj, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
print(clean(si, sj))

