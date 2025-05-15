# 불!
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
walls = []
jihoon_visited = [[0] * M for _ in range(N)]
jihoons = []
fires = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == '#':
            walls.append((i, j))
        elif arr[i][j] == 'J':
            jihoons.append((i, j))
            jihoon_visited[i][j] = 1
        elif arr[i][j] == 'F':
            fires.append((i, j))


def time_spend():
    global fires, jihoons
    '''
    시간 1동안 벌어지는 일 실행
    '''
    # 불 1칸씩만 확산
    # print('시간:', time)
    # print('fires:', fires)
    # print('jihoons:', jihoons)
    next_fires = []
    for i, j in fires:
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '.' or arr[ni][nj] == 'J':
                    next_fires.append((ni, nj))
                    arr[ni][nj] = 'F'
    fires = next_fires
    # 지훈이 이동
    next_jihoons = []
    flag = False
    for i, j in jihoons:
        if i == 0 or i == N-1 or j == 0 or j == M-1:
            print(time + 1)
            return True
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '#' or arr[ni][nj] == 'F':
                    continue
                if ni == 0 or ni == N-1 or nj == 0 or nj == M-1:    # 탈출 가능
                    print(time + 2)
                    return True
                if arr[ni][nj] == '.' and jihoon_visited[ni][nj] == 0:
                    next_jihoons.append((ni, nj))
                    jihoon_visited[ni][nj] = 1
                    flag = True
    jihoons = next_jihoons
    # print(flag)
    if not flag:
        print('IMPOSSIBLE')
        return False

# for r in arr:
#     print(r)
# print()
time = 0
while 1:
    res = time_spend()
    if res is True:
        break
    elif res is False:
        break
    time += 1
    # for r in arr:
    #     print(r)
    # print()