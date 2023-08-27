# 색종이 2
N = int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(N):
    left_bottom, right_top = map(int, input().split())

    # 2차원 배열에 종이 붙여주기(1 넣어주기)
    for i in range(right_top, right_top + 10):
        for j in range(left_bottom, left_bottom + 10):
            arr[i][j] = 1
# for row in arr:
#     print(row)
# 둘레 길이 재기
circum = 0      # 둘레
for i in range(101):
    for j in range(101):
        if arr[i][j] == 0:  # 0일때만 탐색
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:   # 상하좌우 탐색
                ni, nj = i + di, j + dj
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if arr[ni][nj] == 1:    # 상하좌우에 1이 있다면
                        circum += 1         # 둘레 1 추가
print(circum)
