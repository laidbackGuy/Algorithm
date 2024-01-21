def solution(brown, yellow):
    ans = 1
    for i in range(1, (yellow // 2) + 1):
        k = yellow / i
        if brown - (2 * (i+2)) == k * 2:
            ans = i
            break
    # print(ans)
    return [(yellow / ans) + 2, ans + 2]