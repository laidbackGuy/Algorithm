# 주사위 쌓기
import sys
input = sys.stdin.readline

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

table = [[5, 1, 2, 3, 4], [3, 0, 2, 4, 5], [4, 0, 1, 3, 5], [1, 0, 2, 4, 5], [2, 0, 1, 3, 5], [0, 1, 2, 3, 4]]

answer = 0
for fi in range(6):
    bottom = dice[0][fi]
    top = dice[0][table[fi][0]]
    total = max(dice[0][table[fi][1]], dice[0][table[fi][2]], dice[0][table[fi][3]], dice[0][table[fi][4]])
    for floor in range(1, N):
        idx = None
        for j in range(6):
            if dice[floor][j] == top:
                idx = j
                bottom = dice[floor][j]
        top = dice[floor][table[idx][0]]
        total += max(dice[floor][table[idx][1]], dice[floor][table[idx][2]], dice[floor][table[idx][3]], dice[floor][table[idx][4]])
    answer = max(answer, total)
print(answer)