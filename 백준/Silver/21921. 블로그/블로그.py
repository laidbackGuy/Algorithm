# 블로그
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))
now = sum(arr[:X])
left = 0
right = X
cnt = 1
max_v = now

for _ in range(X, N):
    now -= arr[left]
    now += arr[right]
    if now > max_v:
        max_v = now
        cnt = 1
    elif now == max_v:
        cnt += 1
    left += 1
    right += 1
if max_v:
    print(max_v)
    print(cnt)
else:
    print('SAD')