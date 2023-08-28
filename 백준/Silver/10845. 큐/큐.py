# 스택
import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N = int(input())
for i in range(N):
    order = list(input().split())

    if order[0] == 'push':
        queue.append(int(order[1]))
    elif order[0] == 'front':
        if queue:
            print(int(queue[0]))
        else:
            print(-1)
    elif order[0] == 'pop':
        if queue:
            print(int(queue.popleft()))
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order[0] == 'back':
        if queue:
            print(int(queue[-1]))
        else:
            print(-1)