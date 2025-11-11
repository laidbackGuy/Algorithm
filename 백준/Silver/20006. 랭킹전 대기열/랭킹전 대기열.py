# 랭킹전 대기열
import sys
input = sys.stdin.readline

rooms = []  # 방별 인원들의 레벨과 닉네임
table = []  # 방별 게임 시작 상태
room_cnt = 0

p, m = map(int, input().split())
for _ in range(p):
    l, n = input().rstrip().split()
    l = int(l)
    # 입장 가능한 방이 있는지 체크
    if room_cnt > 0:
        for i in range(room_cnt):
            first = rooms[i][0][0]
            if table[i] == 0 and (first - 10 <= l <= first + 10):
                rooms[i].append([l, n])
                if len(rooms[i]) == m:
                    table[i] = 1
                break
        else:
            rooms.append([[l, n]])
            table.append(0)
            if len(rooms[room_cnt]) == m:
                table[room_cnt] = 1
            room_cnt += 1

    else:
        rooms.append([[l, n]])
        table.append(0)
        if len(rooms[room_cnt]) == m:
            table[room_cnt] = 1
        room_cnt += 1


for i in range(room_cnt):
    if table[i] == 1:
        print("Started!")
    elif table[i] == 0:
        print("Waiting!")
    # rooms[i].sort()
    new = sorted(rooms[i], key=lambda x:x[1])
    for l, n in new:
        print(l, n)

# print(rooms)
# print(table)
# print(room_cnt)