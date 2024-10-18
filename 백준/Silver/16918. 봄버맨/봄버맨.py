# 봄버맨

R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
time = 1
bombs = []

didj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            bombs.append((i, j))
while 1:
    if time == N:
        break
    # 빈 칸에 폭탄 심기
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
    time += 1
    if time == N:
        break
    # 3초 전 설치된 폭탄 폭파
    for i, j in bombs:
        arr[i][j] = '.'
        for di, dj in didj:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C:
                arr[ni][nj] = '.'
    time += 1
    if time == N:
        break
    bombs = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                bombs.append((i, j))
for r in arr:
    print(''.join(r))