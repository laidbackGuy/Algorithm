# 컨베이어 벨트 위의 로봇
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr = deque(arr)

broken = 0
turn = 1
robot_idx = deque([0] * N)

while 1:
    # 1번 벨트 한 칸 돌리기
    last = arr.pop()
    arr.appendleft(last)
    robot_idx.pop()
    robot_idx.appendleft(0)
    robot_idx[-1] = 0

    # 2, 3번 로봇 이동
    for i in range(len(robot_idx)-1, -1, -1):
        if robot_idx[i]:
            if i == N-1:
                robot_idx[i] = 0
            else:
                if robot_idx[i+1] == 0 and arr[i+1] >= 1:
                    robot_idx[i] = 0
                    robot_idx[i+1] = 1
                    arr[i+1] -= 1
                    if arr[i+1] == 0:
                        broken += 1
    # 4번
    if arr[0] >= 1:
        robot_idx[0] = 1
        arr[0] -= 1
        if arr[0] == 0:
            broken += 1
    # 5번
    if broken >= K:
        break

    turn += 1
print(turn)