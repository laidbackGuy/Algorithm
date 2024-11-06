# 통계학
import heapq

N = int(input())
sum_v = 0
max_cnt = 1
diff = 0

my_dict = {}
arr = []
for _ in range(N):
    num = int(input())
    if num in my_dict:
        my_dict[num] += 1
        max_cnt = max(max_cnt, my_dict[num])
    else:
        my_dict[num] = 1
    sum_v += num
    arr.append(num)

print(round(sum_v / N))
arr.sort()
print(arr[N//2])
candis = []
for k, v in my_dict.items():
    if v == max_cnt:
        candis.append(k)
if len(candis) == 1:
    print(candis[0])
else:
    candis.sort()
    print(candis[1])
print(max(arr) - min(arr))