# 십자뒤집기
import sys
input = sys.stdin.readline

locs = {0: [0, 1, 3], 1: [0, 1, 2, 4], 2: [1, 2, 5], 3: [0, 3, 4, 6], 4: [1, 3, 4, 5, 7], 5: [2, 4, 5, 8], 6: [3, 6, 7], 7: [4, 6, 7, 8], 8: [5, 7, 8]}


def flip(table, stage, fliped):
    global answer
    if answer:
        return

    if sum(table) == 0:
        answer = fliped
        return

    if stage == 9:
        return

    flip(table, stage + 1, fliped)

    flipped_table = table[:]
    for di in locs[stage]:
        flipped_table[di] = 1 - flipped_table[di]
    flip(flipped_table, stage + 1, fliped + 1)


T = int(input())
for tc in range(T):
    arr = [list(input().rstrip()) for _ in range(3)]
    table = [0] * 9

    num = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '*':
                table[num] = 1
            num += 1
    answer = None
    flip(table, 0, 0)
    print(answer)