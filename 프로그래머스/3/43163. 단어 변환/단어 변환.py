answer = 1e9
flag = False
def solution(begin, target, words):
    global flag
    visited = [0] * len(words)
    
    def dfs(current, target, cnt):
        global answer
        global flag
        if current == target:
            if cnt < answer:
                answer = cnt
            flag = True
            return
        
        if cnt >= answer:
            return
        
        for i in range(len(words)):
            if not visited[i]:
                same_char = 0
                for k in range(len(begin)):
                    if current[k] == words[i][k]:
                        same_char += 1
                if same_char == len(begin) - 1:
                    visited[i] = 1
                    dfs(words[i], target, cnt + 1)
                    visited[i] = 0
    dfs(begin, target, 0)
    if flag is False:
        return 0
    return answer
