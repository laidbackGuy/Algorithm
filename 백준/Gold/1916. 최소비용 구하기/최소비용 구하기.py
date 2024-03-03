#최소비용 구하기
import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])
start_node, goal = map(int, input().split())
distance = [int(1e9)] * (N+1)


def dstra(start):
    pri_q = []

    heapq.heappush(pri_q, (0, start))
    distance[start] = 0

    while pri_q:
        dist, now = heapq.heappop(pri_q)
        if now == goal:
            return distance[now]

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node, cost = next

            new_cost = dist + cost

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pri_q, (new_cost, next_node))

    return distance[goal]


print(dstra(start_node))
