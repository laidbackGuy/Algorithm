# 달팽이
N = int(input())
target = int(input())
arr = [[0] * N for _ in range(N)]
ti, tj = 0, 0
i, j = N // 2, N // 2
dir_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
arr[i][j] = 1
num = 2
dir_limit = 1
cnt = 0
dir = 0
dir_cnt = 0
if target == 1:
    ti, tj = i, j
while num <= N**2:
    i, j = i + dir_list[dir][0], j + dir_list[dir][1]
    if num == target:
        ti, tj = i, j
    arr[i][j] = num
    num += 1
    cnt += 1
    if cnt == dir_limit:
        dir = (dir + 1) % 4
        cnt = 0
        dir_cnt += 1
        if dir_cnt == 2:
            dir_limit += 1
            dir_cnt = 0

for r in arr:
    print(*r)
print(ti+1, tj+1)