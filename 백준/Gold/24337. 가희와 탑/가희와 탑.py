# 가희와 탑
import sys
from collections import deque
input = sys.stdin.readline

N, a, b = map(int, input().split())
if N == 1:
    print(1)
elif a + b > N + 1:
    print(-1)
else:
    buildings = deque([])
    remain = 0

    if a + b < N + 1:
        if a == 1:
            for i in range((N + 1) - (a + b)):
                buildings.append(1)
        else:
            remain = (N + 1) - (a + b)

    buildings.appendleft(max(a, b))

    for floor in range(a-1, 0, -1):
        buildings.appendleft(floor)

    for floor in range(b-1, 0, -1):
        buildings.append(floor)

    for i in range(remain):
        buildings.appendleft(1)

    for n in buildings:
        print(n, end=" ")