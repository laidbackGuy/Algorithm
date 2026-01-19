# 에디터
import sys
from collections import deque
input = sys.stdin.readline

my_str = input().rstrip()
L = len(my_str)
M = int(input())

left = deque(list(my_str))
right = deque([])

for _ in range(M):
    order = input().rstrip()
    if len(order) > 1:
        char = order[2]
        left.append(char)
    else:
        if order == 'L':
            if left:
                right.appendleft(left.pop())
        elif order == 'D':
            if right:
                left.append(right.popleft())
        elif order == 'B':
            if left:
                left.pop()
    # print("".join(left),  "".join(right))
print("".join(left) + "".join(right))