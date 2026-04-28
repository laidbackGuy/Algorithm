def solution(diffs, times, lm):
    answer = 0
    N = len(diffs)
    
    
    def check(lv, limit):
        time_prev = 0
        for i in range(N):
            diff = diffs[i]
            time_cur = times[i]
            
            if diff > lv:
                limit -= ((diff - lv) * (time_prev + time_cur)) + time_cur
            else:
                limit -= time_cur
                
            if limit < 0:
                return False
        
            time_prev = time_cur
            
        return True

    
    left, right = 1, max(diffs)
    while left <= right:
        mid = (left+right)//2
        
        if check(mid, lm):
            right = mid - 1
        else:
            left = mid + 1

    answer = left
    
    return answer