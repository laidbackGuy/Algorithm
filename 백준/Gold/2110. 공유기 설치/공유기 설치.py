# 공유기 설치
import sys, heapq
input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
# heapq.heappush(hq, int(input()))
houses.sort()
max_dist = houses[-1] - houses[0]


def check(min_dist, cnt):
    cnt -= 1
    prev = houses[0]
    for i in range(1, N):
        now = houses[i]
        if now - prev >= min_dist:
            cnt -= 1
            if cnt == 0:
                return 1
            prev = now
    else:
        if cnt > 0:
            return 0


left = 1
right = houses[-1] - houses[0]
while left <= right:
    mid = (left + right) // 2
#    print(left, mid, right)
    if check(mid, C):
        left = mid + 1
    else:
        right = mid - 1

print(right)
# for target in range(1, max_dist + 1):