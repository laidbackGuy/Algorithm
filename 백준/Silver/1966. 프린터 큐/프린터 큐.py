# 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    arr_idx = deque([i for i in range(N)])
    record = [0] * N

    order = 1
    while arr:
        if arr[0] == max(arr):
            arr.popleft()
            out = arr_idx.popleft()
            record[out] = order
            order += 1
        else:
            arr.append(arr.popleft())
            arr_idx.append(arr_idx.popleft())

    print(record[M])
    
