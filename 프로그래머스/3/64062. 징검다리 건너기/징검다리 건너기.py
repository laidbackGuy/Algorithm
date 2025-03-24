def solution(stones, k):
    N = len(stones)
    
    left, right = 1, 200000000
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for num in stones:
            if num <= mid:
                cnt += 1
                if cnt == k:
                    right = mid - 1
                    break
            else:
                cnt = 0
        else:
            left = mid + 1
        
    return left