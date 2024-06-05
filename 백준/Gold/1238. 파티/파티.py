# 파티
import heapq

N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    f, t, w = map(int, input().split())
    adj[f].append((t, w))


def dstra(start, end):
    distance = [1e9] * (N+1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)

        for next, cost in adj[now]:
            new_cost = dist + cost

            if new_cost > distance[next]:
                continue

            distance[next] = new_cost
            heapq.heappush(pq, (new_cost, next))
    return distance[end]


answer = 0
for i in range(1, N+1):
    time = 0
    time += dstra(i, X)
    time += dstra(X, i)
    answer = max(answer, time)

print(answer)