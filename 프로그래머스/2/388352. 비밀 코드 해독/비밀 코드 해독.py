from itertools import combinations


def solution(n, q, ans):
    global answer
    answer = 0
    arr = [i for i in range(1, n+1)]
    
    Q = len(q)
    
    candis = list(combinations(arr, 5))
    for candi in candis:
        for i in range(Q):
            cnt = 0
            for num in candi:
                if num in q[i]:
                    cnt += 1
            if cnt == ans[i]:
                continue
            else:
                break
        else:
            answer += 1
    
    return answer

        

