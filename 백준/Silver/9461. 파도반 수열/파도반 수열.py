# 파도반 수열


def P(n):
    global memo
    if 1 <= n <= 3:
        return 1
    elif 4 <= n <= 5:
        return 2
    else:
        memo[1] = memo[2] = memo[3] = 1
        memo[4] = memo[5] = 2
        for i in range(6, n+1):
            memo[i] = memo[i-2] + memo[i-3]
    return memo[n]


T = int(input())
for tc in range(T):
    N = int(input())
    memo = [0] * (N+1)
    print(P(N))
    # print(memo)