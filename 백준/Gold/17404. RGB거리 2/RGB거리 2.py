# RGB 거리 2
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp_left = [[0] * 3 for _ in range(N)]
dp_center = [[0] * 3 for _ in range(N)]
dp_right = [[0] * 3 for _ in range(N)]


dp_left[0] = arr[0]
dp_left[1][0] = 1e9
dp_left[1][1] = arr[0][0] + arr[1][1]
dp_left[1][2] = arr[0][0] + arr[1][2]

dp_center[0] = arr[0]
dp_center[1][0] = arr[0][1] + arr[1][0]
dp_center[1][1] = 1e9
dp_center[1][2] = arr[0][1] + arr[1][2]

dp_right[0] = arr[0]
dp_right[1][0] = arr[0][2] + arr[1][0]
dp_right[1][1] = arr[0][2] + arr[1][1]
dp_right[1][2] = 1e9

# for r in dp_left:
#     print(r)
# print()
# for r in dp_center:
#     print(r)
# print()
# for r in dp_right:
#     print(r)
# print()
# print()
for i in range(2, N):
    dp_left[i][0] = min(dp_left[i-1][1], dp_left[i-1][2]) + arr[i][0]
    dp_left[i][1] = min(dp_left[i-1][0], dp_left[i-1][2]) + arr[i][1]
    dp_left[i][2] = min(dp_left[i-1][0], dp_left[i-1][1]) + arr[i][2]

    dp_center[i][0] = min(dp_center[i - 1][1], dp_center[i - 1][2]) + arr[i][0]
    dp_center[i][1] = min(dp_center[i - 1][0], dp_center[i - 1][2]) + arr[i][1]
    dp_center[i][2] = min(dp_center[i - 1][0], dp_center[i - 1][1]) + arr[i][2]

    dp_right[i][0] = min(dp_right[i - 1][1], dp_right[i - 1][2]) + arr[i][0]
    dp_right[i][1] = min(dp_right[i - 1][0], dp_right[i - 1][2]) + arr[i][1]
    dp_right[i][2] = min(dp_right[i - 1][0], dp_right[i - 1][1]) + arr[i][2]

# for r in dp_left:
#     print(r)
# print()
# for r in dp_center:
#     print(r)
# print()
# for r in dp_right:
#     print(r)

answer = min(dp_left[N-1][1], dp_left[N-1][2], dp_center[N-1][0], dp_center[N-1][2], dp_right[N-1][0], dp_right[N-1][1])
print(answer)