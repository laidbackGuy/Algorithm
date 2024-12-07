# 예산
import sys
input = sys.stdin.readline

N = int(input())
orders = list(map(int, input().split()))
budget = int(input())

right = max(orders)
left = 1
answer = 0
while left <= right:
    mid = (left + right) // 2
    cur = 0
    flag = True
    for order in orders:
        if order <= mid:
            cur += order
        else:
            cur += mid
        if cur > budget:
            flag = False
            break
    if not flag:
        right = mid - 1
    else:
        answer = max(answer, mid)
        left = mid + 1
print(answer)