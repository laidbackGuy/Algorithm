# 오목
import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]
visited = [[0]*19 for _ in range(19)]


def check(color, i, j):
    for di, dj in [[0, 1], [1, 0], [1, 1], [1, -1]]:
        cnt = 1
        for k in range(1, 5):
            ni, nj = i + di*k, j + dj*k
            if 0 <= ni < 19 and 0 <= nj < 19:
                if arr[ni][nj] != color:
                    # print(ni, nj, '땡')
                    break
                elif arr[ni][nj] == color:
                    # print(ni, nj, '오!')
                    cnt += 1
        # print('cnt:', cnt)
        if cnt == 5:
            check_6 = False

            li, lj = i + di*5, j + dj*5
            if 0 <= li < 19 and 0 <= lj < 19:
                if arr[li][lj] == color:
                    check_6 = True

            pi, pj = i - di, j - dj
            if 0 <= pi < 19 and 0 <= pj < 19:
                if arr[pi][pj] == color:
                    check_6 = True

            if not check_6:
                print(color)
                if di == 1 and dj == -1:
                    print(i+5, j-3)
                else:
                    print(i+1, j+1)
                return True
        # print()
    return False


flag = False
for i in range(19):
    for j in range(19):
        if arr[i][j]:
            res = check(arr[i][j], i, j)
            if res:
                flag = True
                break
    if flag:
        break
if not flag:
    print(0)