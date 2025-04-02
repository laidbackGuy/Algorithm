N = int(input())
arr = list(map(int, input().split()))

sorted_list = sorted(set(arr))
# print(sorted_list)
my_dict = {}

for i in range(len(sorted_list)):
    my_dict[sorted_list[i]] = i

answer = []
for num in arr:
    answer.append(my_dict[num])

print(*answer)