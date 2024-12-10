# 사이클 게임
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [i for i in range(N)]


def find(x):
    while x != parents[x]:
        x = parents[x]
    return x


def union(x, y):
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

answer = 0
for cnt in range(1, M+1):
    a, b = map(int, input().split())
    A = find(a)
    B = find(b)
    if A == B:
        answer = cnt
        break
    else:
        union(A, B)
print(answer)