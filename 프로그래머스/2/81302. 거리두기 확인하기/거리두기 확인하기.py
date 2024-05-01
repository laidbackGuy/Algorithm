# from collections import deque

def dfs(i, j, cnt, arr):
    global visited
    global flag
    
    if cnt != 0 and arr[i][j] == 'P':
        # for r in arr:
        #     print(r)
        # print('위치:', i, j, 'cnt:', cnt)
        # print()
        flag = False
        return
    
    if cnt == 2:
        return
    
    for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 5 and 0 <= nj < 5:
            if visited[ni][nj] == 0 and arr[ni][nj] != 'X':
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1, arr)    
                visited[ni][nj] = 0
                
    
    
def solution(places):
    global visited
    
    global flag
    answer = []
    for place in places:
        flag = True
        
        for i in range(5):
            for j in range(5):
                
                if place[i][j] == 'P':
                    # print('시작:', i, j)
                    visited = [[0]*5 for _ in range(5)]
                    visited[i][j] = 1
                    if dfs(i, j, 0, place) is False:
                        flag = False
                        break
            if flag is False:
                break
       
        if flag is False:
            answer.append(0)
        else:
            answer.append(1)
        
            
    return answer