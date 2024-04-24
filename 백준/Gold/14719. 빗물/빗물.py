# 빗물
H, W = map(int, input().split())
heights = list(map(int, input().split()))
arr = [[0] * W for _ in range(H)]

for i in range(len(heights)):
    for floor in range(heights[i]):
        arr[floor][i] = 1

ans = 0
for i in range(H):
    cnt = 0
    state = False
    for j in range(W):
        if arr[i][j]:
            ans += cnt
            cnt = 0
            state = True
        else:
            if state:
                cnt += 1
print(ans)

