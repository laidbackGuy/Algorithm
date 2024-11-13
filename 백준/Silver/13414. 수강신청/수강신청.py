# 수강신청
import sys
input = sys.stdin.readline

K, L = map(int, input().split())
order = {}
cnt = 1
for _ in range(L):
    now = input().rstrip()
    order[now] = cnt
    cnt += 1
new = {}
for k, v in order.items():
    new[v] = k
for i in sorted(new.keys()):
    print(new[i])
    K -= 1
    if not K:
        break