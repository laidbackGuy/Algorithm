# 주사위 굴리기
def dice(order):
    global cur_dice
    next_dice = {}
    if order == 1:
        next_dice = {1: cur_dice[4], 2: cur_dice[2], 3: cur_dice[1], 4: cur_dice[6], 5: cur_dice[5], 6: cur_dice[3]}
    elif order == 2:
        next_dice = {1: cur_dice[3], 2: cur_dice[2], 3: cur_dice[6], 4: cur_dice[1], 5: cur_dice[5], 6: cur_dice[4]}
    elif order == 3:
        next_dice = {1: cur_dice[5], 2: cur_dice[1], 3: cur_dice[3], 4: cur_dice[4], 5: cur_dice[6], 6: cur_dice[2]}
    elif order == 4:
        next_dice = {1: cur_dice[2], 2: cur_dice[6], 3: cur_dice[3], 4: cur_dice[4], 5: cur_dice[1], 6: cur_dice[5]}
    # print(next_dice)
    cur_dice = next_dice


didj_list = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}

N, M, si, sj, n_order = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
orders = list(map(int, input().split()))

cur_dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# print(arr)
# print(orders)

i, j = si, sj
if arr[i][j] != 0:
    cur_dice[6] = arr[i][j]
for order in orders:
    didj = didj_list[order]
    ni, nj = i + didj[0], j + didj[1]
    if 0 <= ni < N and 0 <= nj < M:
        dice(order)
        i, j = ni, nj
        if arr[i][j] != 0:
            cur_dice[6] = arr[i][j]
            arr[i][j] = 0
        elif arr[i][j] == 0:
            arr[i][j] = cur_dice[6]
        print(cur_dice[1])
