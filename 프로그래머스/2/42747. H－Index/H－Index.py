def solution(citations):
    answer = 0
    h = max(citations)
    n = len(citations)
    cnt_list = [0] * (h + 1)
    
    for i in range(n):
        c = citations[i]
        cnt_list[c] += 1
    
    while 1:
        if sum(cnt_list[h:]) >= h:
            return h
        h -= 1
