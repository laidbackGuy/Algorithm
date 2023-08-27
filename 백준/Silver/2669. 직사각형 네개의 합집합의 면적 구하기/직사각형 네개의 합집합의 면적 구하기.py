# 직사각형 네개의 합집합의 면적 구하기
arr = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x, y, p, q = map(int, input().split())

    # 2차원 배열에 종이 붙여주기(1 넣어주기)
    for i in range(x, p):
        for j in range(y, q):
            arr[i][j] = 1
# for row in arr:
#     print(row)

area = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            area += 1
print(area)
