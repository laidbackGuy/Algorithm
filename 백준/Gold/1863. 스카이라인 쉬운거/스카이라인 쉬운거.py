# 스카이라인 쉬운거
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque([])
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
        answer += 1

    if y > 0:
        if not stack or stack[-1] < y:
            stack.append(y)
answer += len(stack)
print(answer)