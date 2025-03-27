# 과자 나눠주기
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))
left, right = 1, max(snacks)


def check(length):
    cnt = 0
    for s in snacks:
        cnt += s // length
        if cnt >= M:
            return True
    return False


flag = False
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        flag = True
        left = mid + 1
    else:
        right = mid - 1
if not flag:
    print(0)
else:
    print(right)