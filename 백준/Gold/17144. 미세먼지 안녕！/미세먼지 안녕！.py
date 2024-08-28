# 미세먼지 안녕!
import sys, copy
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

top_didj = [[0, 1], [-1, 0], [0, -1], [1, 0]]
bottom_didj = [[0, 1], [1, 0], [0, -1], [-1, 0]]

time = 0
ti, tj, bi, bj = None, None, None, None
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            if ti:
                bi, bj = i, j
            else:
                ti, tj = i, j

while 1:
    new_arr = [[0] * C for _ in range(R)]
    new_arr[ti][tj], new_arr[bi][bj] = -1, -1
    for i in range(R):
        for j in range(C):
            if arr[i][j] and arr[i][j] != -1:
                cnt = 0
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        if arr[ni][nj] != -1:
                            cnt += 1
                            new_arr[ni][nj] += arr[i][j] // 5
                new_arr[i][j] += arr[i][j] - ((arr[i][j] // 5)*cnt)

    arr = copy.deepcopy(new_arr)

    # for r in arr:
    #     print(r)
    # print()
    new_arr = copy.deepcopy(arr)

    top_dir = 0
    ci, cj = ti, tj
    while 1:
        ni, nj = ci + top_didj[top_dir][0], cj + top_didj[top_dir][1]
        if 0 <= ni < R and 0 <= nj < C:
            if ni == ti and nj == tj:
                break
            new_arr[ni][nj] = arr[ci][cj]
            ci, cj = ni, nj
        else:
            top_dir += 1

    bottom_dir = 0
    ci, cj = bi, bj
    while 1:
        ni, nj = ci + bottom_didj[bottom_dir][0], cj + bottom_didj[bottom_dir][1]
        if 0 <= ni < R and 0 <= nj < C:
            if ni == bi and nj == bj:
                break
            new_arr[ni][nj] = arr[ci][cj]
            ci, cj = ni, nj
        else:
            bottom_dir += 1
    new_arr[ti][tj + 1], new_arr[bi][bj + 1] = 0, 0
    arr = copy.deepcopy(new_arr)
    # for r in arr:
    #     print(r)
    # print()
    time += 1
    if time == T:
        break

answer = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] and arr[i][j] != -1:
            answer += arr[i][j]
print(answer)
