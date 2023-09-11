# 수 정렬하기 3
import sys
# sys.stdin = open('input_10989_수 정렬하기 3.txt')

N = int(sys.stdin.readline())
count = {}
for i in range(N):
    num = int(sys.stdin.readline())
    count.setdefault(num, 0)
    count[num] += 1
# print(count) #

sorted_keys = list(count.keys())
sorted_keys.sort()
# print(sorted_keys)

for key in sorted_keys:
    for i in range(count[key]):
        print(key)
