# 뱀
# https://www.acmicpc.net/problem/3190

N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
L = int(input())
orders = []
for _ in range(L):
    a, b = input().split()
    orders.append((int(a), b))

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

cur_dir = 1  # 현재 방향 0, 1, 2, 3 순으로 상, 우, 하, 좌
time = 0
queue = []   # 뱀의 머리를 제외한 좌표를 담을 배열
i, j = 0, 0
arr[0][0] = 8
# for r in arr:
#     print(r)
# print('현재 시각:', time)
# print()
while True:
    # 현재 방향에 맞게 다음 칸 정의
    ni, nj = i + direction[cur_dir][0], j + direction[cur_dir][1]
    
    # 다음 칸이 벽이라면 게임 오버
    if ni < 0 or ni >= N or nj < 0 or nj >= N:
        time += 1
        break

    # 다음 칸이 뱀이라면 게임 오버
    if arr[ni][nj] == 8:
        time += 1
        break

    queue.append((i, j))  # 이전 머리칸을 queue에 저장
    
    if arr[ni][nj] == 0:    # 다음칸이 빈칸이면
        ti, tj = queue.pop(0)    # 꼬리칸 없애기
        arr[ti][tj] = 0

    # 머리는 다음 칸으로 이동
    arr[ni][nj] = 8
    i, j = ni, nj

    time += 1

    # orders 순회하며 현재 초에 실행할 명령어 있으면 명령에 맞게 방향 바꾸기
    for check_time, next_dir in orders:
        if time == check_time:
            if next_dir == 'D':
                cur_dir = (cur_dir + 1) % 4
            else:
                cur_dir -= 1
                if cur_dir == -1:
                    cur_dir = 3

    # for r in arr:
    #     print(r)
    # print('현재 시각:', time)
    # print(queue)
    # print()
print(time)
