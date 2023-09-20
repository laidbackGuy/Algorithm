# N개에서 K개를 고르는 순열
def f(i, N, K):    # i : 이전에 고른 개수
    if i == K:  # 순열 완성 : K개를 모두 고른 경우
        print(*p)
        return
    else:   # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:    # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i + 1, N, K)
                used[j] = 0


N, M = map(int, input().split())

card = [i for i in range(1, N+1)]

used = [0] * N  # 이미 사용한 카드인지 표시
p = [0] * M

f(0, N, M)






