# 고층 건물
import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))
answer = 0

for i in range(N):
    # print('기준:', i)
    now_cnt = 0
    x = i
    y = buildings[i]

    slope = None
    for j in range(i-1, -1, -1):
        dx = j
        dy = buildings[j]
        cur_slope = (y - dy) / (x - dx)
        if cur_slope == -0.0:
            cur_slope = 0
        # print(j, cur_slope)
        if slope is None:
            # print('보임')
            slope = cur_slope
            now_cnt += 1
        else:
            if cur_slope < slope:
                # print('보임')
                slope = cur_slope
                now_cnt += 1

    slope = None
    for j in range(i+1, N):
        dx = j
        dy = buildings[j]
        cur_slope = (y - dy) / (x - dx)
        if cur_slope == -0.0:
            cur_slope = 0
        # print(j, cur_slope)
        if slope is None:
            # print('보임')
            slope = cur_slope
            now_cnt += 1
        else:
            if cur_slope > slope:
                # print(cur_slope, slope, '보임')
                slope = cur_slope
                now_cnt += 1
    # print(now_cnt)
    # print()
    answer = max(answer, now_cnt)

print(answer)