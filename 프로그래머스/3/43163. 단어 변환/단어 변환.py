def solution(begin, target, words):
    global answer
    answer = 1e9
    M = len(words)
    length = len(begin)
    visited = [0] * M
    
    
    def find(now, cnt):
        # print(now)
        global answer
        
        if now == target:
            answer = min(answer, cnt)
        
        if cnt >= answer:
            return
        
        for i in range(M):
            next = words[i]
            # print(next)
            if visited[i] == 0:
                point = 0
                for k in range(length):
                    # print(now[k], next[k])
                    
                    if now[k] != next[k]:
                        point += 1
                        if point > 1:
                            break
                # print(point)
                if point == 1:
                    visited[i] = 1
                    # print(now, next)
                    find(next, cnt + 1)
                    visited[i] = 0
                    
                    
    if target not in words:
        return 0
    
    find(begin, 0)
        
    if answer == 1e9:
        return 0
    
    return answer
    