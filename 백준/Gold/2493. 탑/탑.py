# 탑
import sys, heapq
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
else:
    towers = list(map(int, input().split()))
    table = [0] * N
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (towers[N-1], N-1))
    for i in range(N-2, -1, -1):
        height = towers[i]
        # print(i+1, height)
        while pq:
            now, idx = pq[0]
            # print(now, idx)
            if now <= height:
                heapq.heappop(pq)
                table[idx] = i + 1
                # print(table)
            else:
                break
        heapq.heappush(pq, (towers[i], i))
        # print(pq)
        # print()
    print(*table)
