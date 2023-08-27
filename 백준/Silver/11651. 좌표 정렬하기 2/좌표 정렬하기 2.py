# 좌표 정렬하기2
N = int(input())
yx_dict = {}
for i in range(N):
    x, y = map(int, input().split())
    if y in yx_dict:
        yx_dict[y].append(x)
    else:
        yx_dict[y] = [x]
# print(yx_dict)
keys = []
for k in yx_dict.keys():
    keys.append(k)
keys.sort()
# print(keys)

for y in keys:
    x_list = yx_dict[y]
    x_list.sort()
    for x in x_list:
        print(x, y)
