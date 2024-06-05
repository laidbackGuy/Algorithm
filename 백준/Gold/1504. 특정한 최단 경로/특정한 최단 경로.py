# 특정한 최단경로
import heapq

N, E = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    f, t, w = map(int, input().split())
    adj[f].append((t, w))
    adj[t].append((f, w))
v1, v2 = map(int, input().split())


def dstra(start, end):
    distance = [1e9] * (N + 1)
    pq = [(0, start)]
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        for next, cost in adj[now]:
            new_cost = cost + dist

            if new_cost >= distance[next]:
                continue

            distance[next] = new_cost
            heapq.heappush(pq, (new_cost, next))

    return distance[end]


dist_v1v2 = dstra(v1, v2)

answer = 0
answer_1, answer_2 = dist_v1v2, dist_v1v2

answer_1 += dstra(1, v1)
answer_1 += dstra(v2, N)
answer_2 += dstra(1, v2)
answer_2 += dstra(v1, N)

answer = min(answer_1, answer_2)
if answer >= 1e9:
    answer = -1
print(answer)