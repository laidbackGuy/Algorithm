# 맥주 마시면서 걸어가기
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    global answer
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        # print(x, y, queue)
        fd = abs(fx - x) + abs(fy - y)
        if fd <= 1000:
            answer = 'happy'
            return

        for i in range(n):
            # 방문하지 않은 편의점 중
            if con_stores[i][2] == 0:
                nx = con_stores[i][0]
                ny = con_stores[i][1]
                d = abs(nx - x) + abs(ny - y)
                if d <= 1000:
                    queue.append((nx, ny))
                    con_stores[i][2] = 1


t = int(input())
for tc in range(t):
    n = int(input())
    hx, hy = map(int, input().split())

    con_stores = []
    for _ in range(n):
        con_stores.append(list(map(int, input().split())) + [0])

    fx, fy = map(int, input().split())

    answer = 'sad'

    bfs(hx, hy)

    print(answer)