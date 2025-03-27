# 과자 나눠주기
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))
left, right = 1, max(snacks)


def check(length):
    # global answer
    cnt = 0
    for s in snacks:
        while 1:
            if s >= length:
                s -= length
                cnt += 1
                if cnt == M:
                    # answer = length
                    return True
            else:
                break
    return False


flag = False
# answer = 1
while left <= right:
    mid = (left + right) // 2
    # print(left, mid, right)
    if check(mid):
        flag = True
        left = mid + 1
    else:
        right = mid - 1
    # print(left, mid, right)
    # print()
if not flag:
    print(0)
else:
    # print(answer)
    print(right)