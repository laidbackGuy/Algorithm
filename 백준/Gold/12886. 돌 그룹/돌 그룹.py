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
    visited = [[0] * (total + 1) for _ in range(total + 1)]
    q = deque([(A, B)])
    visited[A][B] = 1
    while q:
        a, b = q.popleft()
        c = total - a - b
        if a == b == c:
            answer = 1
            break
        for x, y in (a, b), (b, c), (a, c):
            if x > y:
                x -= y
                y += y
            elif y > x:
                y -= x
                x += x
            else:
                continue
            z = total - x - y
            a = min(x, y, z)
            b = max(x, y, z)
            if visited[a][b] == 0:
                q.append((a, b))
                visited[a][b] = 1

    print(answer)
