# 어두운 굴다리
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
locs = list(map(int, input().split()))

prev = 0
max_dif = 0
for loc in locs:
    max_dif = max(loc - prev, max_dif)
    prev = loc
# print('max_dif:', max_dif)
if max_dif % 2 == 0:
    max_dif //= 2
else:
    max_dif = ((max_dif // 2) + 1)
side = max(locs[0], N - locs[-1])
# print('side:', side)
if side > max_dif:
    print(side)
else:
    print(max_dif)