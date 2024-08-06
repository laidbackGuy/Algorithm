# 최소비용 구하기2
import heapq
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
adj = deque([[] for _ in range(N+1)])
for _ in range(M):
    f, t, w = map(int, input().split())
    adj[f].append((t, w))
start, target = map(int, input().split())

distance = [[1e9, [], 0] for _ in range(N+1)]


def dstra(s):
    pq = [(0, s, [s])]
    distance[s][0] = 0
    while pq:
        dist, now, route = heapq.heappop(pq)

        if now == target:
            return

        if dist > distance[now][0]:
            continue

        for next, cost in adj[now]:
            new_cost = dist + cost

            if distance[next][0] > new_cost:
                heapq.heappush(pq, (new_cost, next, [*route, next]))
                distance[next][0] = new_cost
                distance[next][1] = [*route, next]

dstra(start)
answer = distance[target]
print(answer[0])
print(len(answer[1]))
print(*answer[1])