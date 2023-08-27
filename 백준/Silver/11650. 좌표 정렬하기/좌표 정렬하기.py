# 좌표 정렬하기
N = int(input())
xy_dict = {}
for i in range(N):
    x, y = map(int, input().split())
    if x in xy_dict:
        xy_dict[x].append(y)
    else:
        xy_dict[x] = [y]
keys = []
for k in xy_dict.keys():
    keys.append(k)
keys.sort()

for x in keys:
    y_list = xy_dict[x]
    y_list.sort()
    for y in y_list:
        print(x, y)
