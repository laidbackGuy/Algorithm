# Yonsei TOTO
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
my_list = []
for _ in range(n):
    P, L = map(int, input().split())
    arr = list(map(int, input().split()))
    if P < L:
        my_list.append(1)
    else:
        arr.sort(reverse=True)
        my_list.append(arr[L-1])
my_list.sort()
answer = 0
for mi in my_list:
    m -= mi
    if m < 0:
        break
    answer += 1
print(answer)
