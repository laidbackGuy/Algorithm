# 미로 만들기
import sys
input = sys.stdin.readline

n = int(input())
orders = input()

arr = [['#'] * ((2*n) + 1) for _ in range((2*n) + 1)]

arr[n][n] = '.'
ci, cj = n, n

top, bottom, left, right = n, n, n, n

didj = [[1, 0], [0, -1], [-1, 0], [0, 1]]
direction = 0

for order in orders:
    if order == 'R':
        direction = (direction + 1) % 4
    elif order == 'L':
        direction -= 1
        if direction < 0:
            direction = 3
    elif order == 'F':
        ci += didj[direction][0]
        cj += didj[direction][1]
        arr[ci][cj] = '.'

        if ci < top:
            top = ci
        if ci > bottom:
            bottom = ci
        if cj < left:
            left = cj
        if cj > right:
            right = cj

for i in range(top, bottom+1):
    for j in range(left, right+1):
        if j == right:
            print(arr[i][j])
        else:
            print(arr[i][j], end='')
    # print(*arr[i][left:right+1])
