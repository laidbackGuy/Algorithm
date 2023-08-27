# 아기 상어
# import sys
# sys.stdin = open('input_16236.txt')


def eat_fish(si, sj):
    global shark_size, time, eat_cnt
    eatable_list = []   # 먹을 수 있는 물고기들의 좌표
    min_dis = 1e9   # 먹을 수 있는 물고기중 가장 가까운 거리

    queue = []
    visited = [[0] * N for _ in range(N)]
    arr[si][sj] = 0
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.pop(0)
        for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:   # 위, 왼쪽, 아래, 오른쪽 순으로 보기
            ni, nj = i + di, j + dj
            # 상어보다 큰 물고기가 아니고 방문한 적이 없다면 갈 수 있음
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= shark_size and visited[ni][nj] == 0:
                if 1 <= arr[ni][nj] < shark_size:  # 먹을 수 있는 물고기라면
                    eatable_list.append((ni, nj))  # 먹을 수 있는 물고기 리스트에 append
                    visited[ni][nj] = visited[i][j] + 1  # visited에 거리 표시
                    if min_dis > visited[ni][nj] - 1:   # 먹을 수 있는 물고기 중 가장 가까운 거리 찾기
                        min_dis = visited[ni][nj] - 1
                queue.append((ni, nj))
                # print(queue)
                visited[ni][nj] = visited[i][j] + 1     # visited에 거리 표시
    # for row in visited:
    #     print(row)
    nearest_eatable_list = []   # 먹을 수 있는 가장 가까운 물고기들의 좌표 리스트
    if eatable_list:    # 먹을 수 있는 물고기가 있었다면
        for i, j in eatable_list:
            if visited[i][j] - 1 == min_dis:
                nearest_eatable_list.append((i, j))
        nearest_eatable_list.sort()     # 먹을 수 있는 물고기 좌표를 위, 왼쪽 우선으로 정렬하여
        # print(eatable_list)
        i, j = nearest_eatable_list.pop(0)
        # print('shark :', shark_size)
        arr[i][j] = 9   # 먹고 이동
        time += (visited[i][j] - 1)  # 걸린 시간 더해주기
        eat_cnt += 1  # 먹은 물고기 수 더해주기
        if eat_cnt == shark_size:  # 상어 크기만큼 물고기를 먹었으면
            shark_size += 1  # 상어 크기 1 키우고
            # print(shark_size)
            eat_cnt = 0  # 먹은 물고기 수 초기화
        return True     # 먹었다면 True 반환
    return False    # 못 먹었다면 False 반환


def find_shark():
    # 상어 좌표 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return i, j


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0    # 현재 초
shark_size = 2    # 상어 현재 사이즈
eat_cnt = 0     # 먹은 물고기 수

while True:
    # 상어 시작점 찾기 -> 물고기 하나 먹기 싸이클 반복
    si, sj = find_shark()
    res = eat_fish(si, sj)
    # for row in arr:
    #     print(row)
    # print(res)
    if res is False:    # 먹을 수 있는 물고기가 없다면 반복 중지
        break
print(time)