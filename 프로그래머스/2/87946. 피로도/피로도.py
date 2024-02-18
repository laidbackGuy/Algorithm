answer = 0
def solution(k, dungeons):
    global answer
    visited = [0] * len(dungeons)
    
    def brute_force(k, cnt, visited):
        global answer
        for i in range(len(dungeons)):
            if k >= dungeons[i][0] and visited[i] == 0:
                visited[i] = 1  # 방문처리
                brute_force(k - dungeons[i][1], cnt + 1, visited)
                visited[i] = 0  # 미방문처리 
        if cnt > answer:
            answer = cnt

    brute_force(k, 0, visited)
    return answer
    