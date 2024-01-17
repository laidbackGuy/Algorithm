def solution(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        j = i
        while cnt <= n:
            cnt += j
            if cnt == n:
                answer += 1
                break
            elif cnt > n:
                break
            j += 1
    return answer