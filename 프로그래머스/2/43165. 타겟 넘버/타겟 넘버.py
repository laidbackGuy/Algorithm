res = 0
def dfs(cnt, cur, target, n, numbers):
    global res
    if cnt == n-1:
        if cur == target:
            res += 1
        return
    
    dfs(cnt+1, cur+numbers[cnt+1], target, n, numbers)
    dfs(cnt+1, cur-numbers[cnt+1], target, n, numbers)
    
            
def solution(numbers, target):
    global res
    answer = 0
    
    dfs(0, numbers[0], target, len(numbers), numbers)
    dfs(0, -numbers[0], target, len(numbers), numbers)
        
    return res