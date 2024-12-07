# 예산
import sys
input = sys.stdin.readline

N = int(input())
orders = list(map(int, input().split()))
budget = int(input())

total = sum(orders)
right = max(orders)
if total <= budget:
    print(right)
else:
    left = 1
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cur = 0
        flag = True
        # print(left, mid, right)
        # print('mid:', mid)
        for order in orders:
            if order <= mid:
                cur += order
            else:
                cur += mid
            if cur > budget:
                flag = False
                # print('cur:', cur)
                break
        if not flag:
            # print('배정 실패')
            right = mid - 1
        else:
            # print('배정 성공')
            answer = max(answer, mid)
            left = mid + 1
    print(answer)