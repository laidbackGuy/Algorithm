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
    # print(i, stack)

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
#     print(i, stack)
#
# print(cnts)
# print(nearest)

# 정방향 체크
# max_h = 0
# max_idx = 0
# stack = deque([])
# for i in range(1, N+1):
#     now_h = heights[i]
#     # print(i, now_h)
#     if now_h < max_h:
#         flag = False
#         while stack:
#             recent_h, recent_cnt, recent_idx = stack[-1][0], stack[-1][1], stack[-1][2]
#             # 최근 뭔가 보였던 탑의 높이가 더 높을 때
#             if now_h < recent_h:
#                 nearest[i] = recent_idx
#                 cnts[i] = recent_cnt + 1
#                 stack.append((now_h, recent_cnt + 1, i))
#                 # print(nearest[i])
#                 flag = True
#                 break
#             else:
#                 stack.pop()
#         # stack 안에서 now보다 큰 높이를 못 만났다면
#         if flag is False:
#             stack = deque([])
#             nearest[i] = max_idx
#             cnts[i] = 1
#             stack.append((now_h, 1, i))
#             # print(nearest[i])
#     else:
#         stack = []
#         max_h = now_h
#         max_idx = i
#     # print('for문 끝나고', stack)
#     # print()
# # print(cnts)
# # print(nearest)
#
# # print()
# # print()
# # 역방향 체크
# max_h = 0
# max_idx = 0
# stack = deque([])
# for i in range(N, 0, -1):
#     now_h = heights[i]
#     # print(i, now_h)
#     if now_h < max_h:
#         flag = False
#         while stack:
#             recent_h, recent_cnt, recent_idx = stack[-1][0], stack[-1][1], stack[-1][2]
#             # 최근 뭔가 보였던 탑의 높이가 더 높을 때
#             if now_h < recent_h:
#                 if nearest[i] != 0:
#                     left = abs(i - nearest[i])
#                     right = abs(i - recent_idx)
#                     if left > right:
#                         nearest[i] = recent_idx
#                 # print(nearest[i])
#                 cnts[i] += recent_cnt + 1
#                 stack.append((now_h, recent_cnt + 1, i))
#                 flag = True
#                 break
#             else:
#                 stack.pop()
#             # stack 안에서 now보다 큰 높이를 못 만났다면
#         if flag is False:
#             stack = deque([])
#             stack.append((now_h, 1, i))
#             if nearest[i] == 0:
#                 nearest[i] = max_idx
#             else:
#                 left = abs(i - nearest[i])
#                 right = abs(i - max_idx)
#                 if left > right:
#                     nearest[i] = max_idx
#             # print(nearest[i])
#             cnts[i] += 1
#     else:
#         stack = []
#         max_h = now_h
#         max_idx = i
    # print('for문 끝나고', stack)
# print(cnts)
# print(nearest)

for i in range(1, N+1):
    if nearest[i]:
        print(cnts[i], nearest[i])
    else:
        print(cnts[i])