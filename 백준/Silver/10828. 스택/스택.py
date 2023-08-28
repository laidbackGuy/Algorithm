# 스택
import sys
from collections import deque
input = sys.stdin.readline

stack = []
N = int(input())
for i in range(N):
    order = list(input().split())

    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'top':
        if stack:
            print(int(stack[-1]))
        else:
            print(-1)
    elif order[0] == 'pop':
        if stack:
            print(int(stack.pop()))
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)