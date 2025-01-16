# 식당 입구 대기 줄
import sys
from collections import deque
input = sys.stdin.readline

max_len = 0
back_guy = 1e9

n = int(input())
line = deque([])
for _ in range(n):
    arr = list(map(int, input().split()))
    if len(arr) == 2:
        student = arr[1]
        line.append(student)
        now_len = len(line)
        if now_len > max_len:
            max_len = now_len
            back_guy = line[-1]
        elif now_len == max_len:
            back_guy = min(line[-1], back_guy)
    else:
        line.popleft()


print(max_len, back_guy)