# 랜선 자르기
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

left = 1
right = max(lines)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    flag = False
    for line in lines:
        cnt += (line // mid)
        if cnt >= N:
            flag = True
            break
    if flag:
        left = mid + 1
    else:
        right = mid - 1
print(right)