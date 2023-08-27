# 설탕 배달
num_bong = []
N = int(input())
for i in range(1001):
    for j in range(1668):
        if 5*i + 3*j == N:
            num_bong.append(i + j)
if num_bong:
    print(min(num_bong))
else:
    print(-1)