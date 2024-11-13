# 숫자 정사각형
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

flag = False
max_range = min(N, M)
for k in range(max_range, 1, -1):
    for i in range(N-k+1):
        for j in range(M-k+1):
            # print(i, j)
            # print(i, j+k-1)
            # print(i+k-1, j)
            # print(i+k-1, j+k-1)
            if arr[i][j] == arr[i][j+k-1] == arr[i+k-1][j] == arr[i+k-1][j+k-1]:
                print(k**2)
                flag = True
                break
        if flag:
            break
    if flag:
        break
else:
    print(1)