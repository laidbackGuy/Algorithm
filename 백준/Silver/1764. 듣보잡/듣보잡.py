# 듣보잡
# import sys
# input = sys.stdin.readline

N, M = map(int, input().strip().split())
name_dict = {}

for _ in range(N):
    name = input()
    name_dict[name] = 1
    # print(name)
for _ in range(M):
    name = input()
    if name in name_dict:
        name_dict[name] = 2
    # print(name)
DBJ_name = []
for k, v in name_dict.items():
    if v == 2:
        DBJ_name.append(k)

DBJ_name.sort()
# print(DBJ_name)
print(len(DBJ_name))
for name in DBJ_name:
    print(name)
