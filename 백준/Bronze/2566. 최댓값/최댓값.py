arr = [list(map(int, input().split())) for _ in range(9)]
# print(arr)
max_num = 0
max_i, max_j = None, None
for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_num:
            max_num = arr[i][j]
            max_i = i+1
            max_j = j+1
print(max_num)
print(max_i, max_j)
