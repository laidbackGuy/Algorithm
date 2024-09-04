# 부분합
import sys, copy
input = sys.stdin.readline

N, S = map(int, input().split())
sequence = list(map(int, input().split()))

answer = 1e9
flag = False

for num in sequence:
    if num >= S:
        answer = 1
        flag = True
        break

if not flag:
    left = 0
    right = 1
    direc = 'R'
    now = sequence[0] + sequence[1]


    while 1:
        # print(left, right, now)
        check = False
        if now < S:
            if right < N-1:
                right += 1
                now += sequence[right]
                check = True
        elif now >= S:
            # print('boom', left, right)
            answer = min(answer, right - left + 1)
            flag = True
            if answer == 2:
                break
            # print(answer)
            if left < right:
                now -= sequence[left]
                left += 1
                check = True
        if not check:
            break

if not flag:
    answer = 0

print(answer)
