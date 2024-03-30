# 최단경로
# 그냥 다익스트라 문제인듯
import heapq
# from collections import deque

V, E = map(int, input().split())
start = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

INF = 1e9
distance = [INF] * (V+1)

def djkstra(s):
    pq = []
    heapq.heappush(pq, (0, s))
    distance[s] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in adj[now]:
            next_node, cost = next

            new_cost = dist + cost

            if new_cost >= distance[next_node]:
                continue

            heapq.heappush(pq, (new_cost, next_node))
            distance[next_node] = new_cost


djkstra(start)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])