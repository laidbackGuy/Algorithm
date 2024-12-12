# 숨바꼭질 2
from collections import deque

N, K = map(int, input().split())
limit = (K*2) + 1


def bfs(start, target):
    queue = deque([start])
    cnt = 0
    while queue:
        now = queue.popleft()
        if now == target:
            cnt += 1
            continue
        for next in [now + 1, now - 1, now * 2]:
            if 0 <= next <= limit:
                if visited[next] == -1 or visited[now] + 1 == visited[next]:
                    queue.append(next)
                    visited[next] = visited[now] + 1
    return cnt


if N > K:
    print(N - K)
    print(1)
else:
    visited = [-1] * (limit+1)
    visited[N] = 0
    res = bfs(N, K)
    # print(visited)
    print(visited[K])
    print(res)