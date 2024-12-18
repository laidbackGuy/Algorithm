# 파스칼 삼각형
import sys
input = sys.stdin.readline

R, C, W = map(int, input().split())
pascal = [[0] * i for i in range(1, 32)]
pascal[0][0], pascal[1][0], pascal[1][1] = 1, 1, 1
for i in range(2, 31):
    pascal[i][0], pascal[i][i] = 1, 1
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
answer = 0
for i in range(W+1):
    for j in range(i):
        answer += pascal[R + i - 2][C + j - 1]
print(answer)