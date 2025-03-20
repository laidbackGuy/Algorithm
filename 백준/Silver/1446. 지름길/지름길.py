# 지름길
import sys, heapq
# from collections import deque
input = sys.stdin.readline

N, D = map(int, input().split())
adj = [[(i+1, 1)] for i in range(D+1)]
for _ in range(N):
    u, v, w = map(int, input().split())
    if v > D:
        continue
    adj[u].append((v, w))
distance = [10000] * (D+1)
distance[0] = 0


def dstra():
    pq = [(0, 0)]
    while pq:
        now, dist = heapq.heappop(pq)
        if now == D:
            return
        for next, cost in adj[now]:
            if next > D:
                continue
            new_cost = dist + cost
            if new_cost >= distance[next]:
                continue
            heapq.heappush(pq, (next, new_cost))
            distance[next] = new_cost


dstra()
print(distance[D])