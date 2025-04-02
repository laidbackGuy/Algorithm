# 문자열 게임2
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    W = input().rstrip()
    K = int(input())
    N = len(W)

    my_dict = {}
    for i in range(N):
        now = W[i]
        if now in my_dict:
            my_dict[now].append(i)
        else:
            my_dict[now] = [i]

    stst = 10000
    lgst = 0
    for k, v in my_dict.items():
        leng = len(v)
        if leng >= K:
            # print(v)
            for j in range(leng - K + 1):
                candi = v[j:j + K]
                # print('후보군', candi)
                cur_leng = candi[-1] - candi[0] + 1
                # print('지금꺼 길이', cur_leng)
                stst = min(stst, cur_leng)
                lgst = max(lgst, cur_leng)
    if not lgst:
        print(-1)
    else:
        print(stst, lgst)