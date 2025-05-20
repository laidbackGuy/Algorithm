# 감시
import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

didj = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def calc(arr):
    '''
    cctv 시야가 기록된 2차원 배열을 받아서
    시각지대의 크기를 계산하여 return해주는 함수
    '''
    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                res += 1
    return res


def operate(order):
    '''
    cctv별로 방향 정보를 담은 배열을 받아
    2차원 배열에 cctv의 시야를 표시하여 return해주는 함수
    '''
    global answer

    arr = copy.deepcopy(office)

    for i in range(cctv_cnt):
        direction = order[i]
        i, j, cctv_type = cctv_table[i][0], cctv_table[i][1], cctv_table[i][2]

        if cctv_type == 1:
            di, dj = didj[direction]
            flag = True
            for k in range(max_range):
                ni, nj = i + (di * k), j + (dj * k)
                if not (0 <= ni < N and 0 <= nj < M):
                    break
                if arr[ni][nj] == 6:
                    break
                arr[ni][nj] = '#'

        elif cctv_type == 2:
            di, dj = didj[direction]
            for k in range(max_range):
                ni, nj = i + (di*k), j + (dj*k)
                if not (0 <= ni < N and 0 <= nj < M):
                    break
                if arr[ni][nj] == 6:
                    break
                arr[ni][nj] = '#'
            for k in range(max_range):
                ni, nj = i - (di * k), j - (dj * k)
                if not (0 <= ni < N and 0 <= nj < M):
                    break
                if arr[ni][nj] == 6:
                    break
                arr[ni][nj] = '#'

        elif cctv_type == 3:
            for d in range(2):
                direction += 1
                if direction == 4:
                    direction = 0
                di, dj = didj[direction]
                for k in range(max_range):
                    ni, nj = i + (di * k), j + (dj * k)
                    if not (0 <= ni < N and 0 <= nj < M):
                        break
                    if arr[ni][nj] == 6:
                        break
                    arr[ni][nj] = '#'

        elif cctv_type == 4:
            for d in range(3):
                direction += 1
                if direction == 4:
                    direction = 0
                di, dj = didj[direction]
                for k in range(max_range):
                    ni, nj = i + (di * k), j + (dj * k)
                    if not (0 <= ni < N and 0 <= nj < M):
                        break
                    if arr[ni][nj] == 6:
                        break
                    arr[ni][nj] = '#'

        elif cctv_type == 5:
            for d in range(4):
                di, dj = didj[d]
                for k in range(max_range):
                    ni, nj = i + (di * k), j + (dj * k)
                    if not (0 <= ni < N and 0 <= nj < M):
                        break
                    if arr[ni][nj] == 6:
                        break
                    arr[ni][nj] = '#'

    answer = min(calc(arr), answer)


def rec(order, cnt):
    '''
    cctv를 회전시키는 모든 경우의 수를 조합한 배열을 만들어
    operate함수를 실행시키는 함수
    '''
    if cnt == cctv_cnt:
        operate(order)
        return
    cctv_type = cctv_table[cnt][2]
    if cctv_type == 5:
        rec(order + [0], cnt + 1)
    elif cctv_type == 2:
        rec(order + [0], cnt + 1)
        rec(order + [1], cnt + 1)
    else:
        rec(order + [0], cnt + 1)
        rec(order + [1], cnt + 1)
        rec(order + [2], cnt + 1)
        rec(order + [3], cnt + 1)


arr = copy.deepcopy(office)
cctv_table = []
walls = []
num = 0
cctv_cnt = 0
for i in range(N):
    for j in range(M):
        if office[i][j] != 0:
            now = office[i][j]
            if now == 6:
                walls.append((i, j))
            else:
                cctv_table.append((i, j, now))
                num += 1
                cctv_cnt += 1

max_range = max(N, M)
answer = 64
rec([], 0)
print(answer)