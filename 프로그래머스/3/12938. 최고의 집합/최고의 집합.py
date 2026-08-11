def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    remain = s % n
    if remain == 0:
        answer = [s // n] * n
    else:
        answer = ([s // n] * (n - remain)) + ([(s // n) + 1] * remain)
        
    return answer