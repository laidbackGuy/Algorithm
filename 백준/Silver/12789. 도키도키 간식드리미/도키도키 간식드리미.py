# 도키도키 간식드리미
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))
line = deque(line)
stack = deque([])

next = 1
while 1:
    now = line[0]
    # print(line)
    # print(now)
    if now == next:
        line.popleft()
        next += 1
    else:
        if stack:
            if stack[-1] == next:
                # print('ㅇㅇ')
                # print(stack[-1])
                stack.pop()
                next += 1
                # print(next)

            else:
                line.popleft()
                stack.append(now)
        else:
            line.popleft()
            stack.append(now)
    # print(stack)
    # print()
    if not line:
        break

if stack:
    for i in range(len(stack) - 1, -1, -1):
        # print(stack[i])
        if stack[i] != next:
            print('Sad')
            break
        else:
            next += 1
    else:
        print('Nice')
else:
    print('Nice')