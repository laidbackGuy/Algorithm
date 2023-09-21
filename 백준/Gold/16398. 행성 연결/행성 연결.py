# 행성 연결
import heapq

def prim(start):
    heap = []
    MST = [0] * N    # MST에 포함되었는지 여부(Visited와 같음)

    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))

    sum_weight = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(N):
             # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight


N = int(input())
# 인접행렬
graph = [list(map(int, input().split())) for _ in range(N)]
# print(graph)
res = prim(0)
print(res)