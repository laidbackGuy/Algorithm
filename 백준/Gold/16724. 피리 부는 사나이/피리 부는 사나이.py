# 피리 부는  사나이
import sys
from collections import deque
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
numbers = [[0] * M for _ in range(N)]
parents = [i for i in range((M*N)+1)]
number = 0
for i in range(N):
    for j in range(M):
        number += 1
        numbers[i][j] = number
answer = 0
number = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'D':
            union(numbers[i][j], numbers[i+1][j])
        elif board[i][j] == 'U':
            union(numbers[i][j], numbers[i - 1][j])
        elif board[i][j] == 'R':
            union(numbers[i][j], numbers[i][j+1])
        elif board[i][j] == 'L':
            union(numbers[i][j], numbers[i][j-1])

for i in range(1, (M*N)+1):
    if parents[i] == i:
        answer += 1
print(answer)