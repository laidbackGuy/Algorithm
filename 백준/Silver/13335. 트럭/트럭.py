# 트럭
import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
locs = [0] * n
bridge = deque([])
time = 0
temp = 0
while temp < n:
    now = trucks[temp]
    # 다리에 트럭을 더 올릴 수 있으면 올리기
    if sum(bridge) + now <= L:
        bridge.append(now)
        locs[temp] = 1
        temp += 1
        for k in range(n):
            if locs[k]:
                if locs[k] != w + 1:
                    locs[k] += 1
                    if locs[k] == w + 1:
                        bridge.popleft()
            else:
                break
        time += 1
    # 올릴 수 없으면 빨리감기(제일 앞에 있는 트럭이 빠질 때까지)
    else:
        gap = 0
        for k in range(n):
            if locs[k]:
                if locs[k] != w + 1:
                    if gap:
                        locs[k] += gap
                    else:
                        gap = w + 1 - locs[k]
                        locs[k] = w + 1
                        bridge.popleft()
                else:
                    continue
            else:
                break
        time += gap
print(time + w)

