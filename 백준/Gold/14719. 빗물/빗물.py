# 빗물
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
h = list(map(int, input().split()))

if W <= 2:
    print(0)
else:
    answer = 0

    cur_max = h[0]
    stack = []
    for i in range(1, W):
        now = h[i]
        if now >= cur_max:
            for deep in stack:
                answer += (cur_max - deep)
            stack = []
            cur_max = now
        else:
            stack.append(now)

    cur_max = h[W-1]
    stack = []
    for i in range(W-2, -1, -1):
        now = h[i]
        if now > cur_max:
            for deep in stack:
                answer += (cur_max - deep)
            stack = []
            cur_max = now
        else:
            stack.append(now)

    print(answer)