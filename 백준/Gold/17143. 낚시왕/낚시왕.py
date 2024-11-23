# 낚시왕
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
shark_roc = []
shark_info = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark_roc.append([r, c])
    shark_info.append([s, d, z, 1])


def shark_move(i, r, c, s, d):
    if d == 1:
        if r - s < 1:
            unit = R - 1
            s -= (r - 1)
            quot = s // unit
            remain = s % unit
            if quot % 2 == 0:
                r = 1 + remain
                shark_info[i][1] = 2
            else:
                r = R - remain
        else:
            r -= s
    elif d == 2:
        if r + s > R:
            unit = R - 1
            s -= (R - r)
            quot = s // unit
            remain = s % unit
            if quot % 2 == 1:
                r = 1 + remain
            else:
                r = R - remain
                shark_info[i][1] = 1
        else:
            r += s
    if d == 3:
        if c + s > C:
            unit = C - 1
            s -= (C - c)
            quot = s // unit
            remain = s % unit
            if quot % 2 == 1:
                c = 1 + remain
            else:
                c = C - remain
                shark_info[i][1] = 4
        else:
            c += s
    elif d == 4:
        if c - s < 1:
            unit = C - 1
            s -= (c - 1)
            quot = s // unit
            remain = s % unit
            if quot % 2 == 0:
                c = 1 + remain
                shark_info[i][1] = 3
            else:
                c = C - remain
        else:
            c -= s
    return r, c


def fishing():
    global answer
    fj = 0
    while fj <= C:
        # print('fj:', fj)
        # 낚시왕 이동
        fj += 1
        # 땅이랑 가장 가까운 상어 잡기
        min_i = 1e9
        target_i = None
        for i in range(M):
            if shark_info[i][3]:
                now_i = shark_roc[i][0]
                now_j = shark_roc[i][1]
                if fj == now_j:
                    if min_i > now_i:
                        min_i = now_i
                        target_i = i
        # print(target_i)
        if target_i is not None:
            # print(target_i, '버억')
            shark_info[target_i][3] = 0
            answer += shark_info[target_i][2]

        # 상어 이동
        roc_dict = {}
        together_rocs = []
        for i in range(M):
            if shark_info[i][3]:
                # print(i)
                # print(shark_roc[i][0], shark_roc[i][1])
                ni, nj = shark_move(i, shark_roc[i][0], shark_roc[i][1], shark_info[i][0], shark_info[i][1])
                if (ni, nj) in roc_dict:
                    together_rocs.append((ni, nj))
                    roc_dict[(ni, nj)][0] += 1
                    roc_dict[(ni, nj)][1].append(i)
                else:
                    roc_dict[(ni, nj)] = [1, [i]]
                shark_roc[i][0], shark_roc[i][1] = ni, nj
                # print(ni, nj)
                # print()

        # print(roc_dict)
        # 겹치는 상어 잡아먹기
        for roc in together_rocs:
            max_size = 0
            target_i = None
            for i in roc_dict[roc][1]:
                size = shark_info[i][2]
                if size > max_size:
                    max_size = size
                    target_i = i
            for i in roc_dict[roc][1]:
                if i != target_i:
                    shark_info[i][3] = 0
                    # print(f'{target_i}가 {i} 먹음')
        # print(shark_roc)
        # print(shark_info)
        # print()

answer = 0
fishing()
print(answer)