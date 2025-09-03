# 탑 보기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
heights = [0] + list(map(int, input().split()))

cnts = [0] * (N+1)
nearest = [0] * (N+1)

# 정방향
stack = deque([])
for i in range(1, N+1):
    now_h = heights[i]
    if not stack:
        stack.append((now_h, 0, i))
    else:
        while stack:
            recent_h, recent_cnt, recent_idx = stack[-1][0], stack[-1][1], stack[-1][2]
            if now_h < recent_h:
                cnts[i] = recent_cnt + 1
                nearest[i] = recent_idx
                stack.append((now_h, recent_cnt + 1, i))
                break
            else:
                stack.pop()
        else:
            stack.append((now_h, 0, i))

# 역방향
stack = deque([])
for i in range(N, 0, -1):
    now_h = heights[i]
    if not stack:
        stack.append((now_h, 0, i))
    else:
        while stack:
            recent_h, recent_cnt, recent_idx = stack[-1][0], stack[-1][1], stack[-1][2]
            if now_h < recent_h:
                cnts[i] += recent_cnt + 1
                if nearest[i] != 0:
                    left_near = i - nearest[i]
                    right_near = recent_idx - i
                    if right_near < left_near:
                        nearest[i] = recent_idx
                else:
                    nearest[i] = recent_idx
                stack.append((now_h, recent_cnt + 1, i))
                break
            else:
                stack.pop()
        else:
            stack.append((now_h, 0, i))

for i in range(1, N+1):
    if nearest[i]:
        print(cnts[i], nearest[i])
    else:
        print(cnts[i])