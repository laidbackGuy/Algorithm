answer = 1e9
flag = False
def solution(begin, target, words):
    visited = [0] * len(words)
    
    def dfs(current, target, cnt):
        global answer, flag
        
        if current == target:   # target이 되었을 때 return
            if cnt < answer:    # cnt 최솟값 찾기
                answer = cnt
            flag = True         # target에 도달 가능하다고 flag 세우기
            return
        
        if cnt >= answer:       # 가지치기(cnt가 기존 최솟값을 이미 넘어갔다면 return)
            return
        
        for i in range(len(words)):
            if not visited[i]:  # 방문한 적 없는 단어만 가기
                same_char = 0
                for k in range(len(begin)):         # 알파벳 한개만 다른 단어 찾기
                    if current[k] == words[i][k]:
                        same_char += 1
                if same_char == len(begin) - 1: 
                    visited[i] = 1                  # 방문 처리
                    dfs(words[i], target, cnt + 1)  # 다음 재귀
                    visited[i] = 0                  # 미방문 처리
                    
    dfs(begin, target, 0)
    
    if flag is False:
        return 0
    
    return answer
