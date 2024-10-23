# 창고 다각형

N = int(input())
arr = [0] * 1001
max_L = 0
for _ in range(N):
    L, H = map(int, input().split())
    max_L = max(max_L, L)
    arr[L] = H

max_H = max(arr)
max_H_i = []
for i in range(1, max_L+1):
    if arr[i] == max_H:
        max_H_i.append(i)
answer = 0
left_max_i = min(max_H_i)
right_max_i = max(max_H_i)
answer += max_H * ((right_max_i - left_max_i) + 1)

cur_H = 0
cnt = 0
for i in range(1, left_max_i + 1):
    if arr[i] > cur_H:
        answer += cur_H * (cnt + 1)
        cnt = 0
        cur_H = arr[i]
    else:
        if cur_H:
            cnt += 1

cur_H = 0
cnt = 0
for i in range(max_L, right_max_i - 1, -1):
    if arr[i] > cur_H:
        answer += cur_H * (cnt + 1)
        cnt = 0
        cur_H = arr[i]
    else:
        if cur_H:
            cnt += 1
print(answer)