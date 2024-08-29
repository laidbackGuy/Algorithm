# 줄 세우기
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

answer = []

while len(answer) < N:
    queue = deque([])

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        answer.append(now)

        for next in adj[now]:
            indegree[next] -= 1
            if not indegree[next]:
                queue.append(next)
print(*answer)