# 돌 그룹
import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())
answer = 0
total = A + B + C
if total % 3 != 0:
    print(answer)
else:
    share = total // 3
    arr = [A, B, C]
    arr.sort()
    visited = [[0] * (total + 1) for _ in range(total + 1)]
    q = deque([(arr[0], arr[1])])
    visited[arr[0]][arr[1]] = 1
    while q:
        a, b = q.popleft()
        c = total - a - b
        # print(a, b, c)
        if a == b == c:
            answer = 1
            break
        if b != c:
            now = []
            if b < c:
                now.append(b * 2)
                now.append(c - b)
            else:
                now.append(c * 2)
                now.append(b - c)
            now.sort()
            if visited[now[0]][now[1]] == 0:
                q.append(now)
                visited[now[0]][now[1]] = 1
        if a != c:
            now = []
            if a < c:
                now.append(a * 2)
                now.append(c - a)
            else:
                now.append(c * 2)
                now.append(a - c)
            now.sort()
            if visited[now[0]][now[1]] == 0:
                q.append(now)
                visited[now[0]][now[1]] = 1
        if a != b:
            now = []
            if a < b:
                now.append(a * 2)
                now.append(b - a)
            else:
                now.append(b * 2)
                now.append(a - b)
            now.sort()
            if visited[now[0]][now[1]] == 0:
                q.append(now)
                visited[now[0]][now[1]] = 1
    print(answer)
