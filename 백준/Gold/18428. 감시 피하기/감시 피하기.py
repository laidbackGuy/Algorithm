# 감시 피하기
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().split()) for _ in range(N)]


def watch(i, j):
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        for k in range(1, N):
            ni, nj = i + di*k, j + dj*k
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 'O':
                    break
                if arr[ni][nj] == 'S':
                    return False
    return True


blank_list = []
teacher_list = []
student_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teacher_list.append((i, j))
        elif arr[i][j] == 'S':
            student_list.append((i, j))
        else:
            blank_list.append((i, j))

candis = list(combinations(blank_list, 3))

answer = 'NO'
for candi in candis:
    for i, j in candi:
        arr[i][j] = 'O'

    for ti, tj in teacher_list:
        if not watch(ti, tj):
            break
    else:
        answer = 'YES'
        break

    for i, j in candi:
        arr[i][j] = 'X'

print(answer)