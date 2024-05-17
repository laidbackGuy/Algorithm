# 녹색 옷 입은 애가 젤다지?
import heapq


def dijkstra(si, sj):
    # 2. 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (arr[si][sj], si, sj))
    distance[si][sj] = arr[si][sj]

    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, i, j = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[i][j] < dist:
            continue

        # 인접 노드를 확인
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:

                # next_node로 가기 위한 누적 거리
                new_cost = dist + arr[ni][nj]

                # 누적 거리가 기존보다 크네?
                if distance[ni][nj] <= new_cost:
                    continue

                distance[ni][nj] = new_cost
                heapq.heappush(pq, (new_cost, ni, nj))

tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1e9] * N for _ in range(N)]

    dijkstra(0, 0)
    res = distance[N-1][N-1]
    print(f'Problem {tc}: {res}')
    tc += 1
