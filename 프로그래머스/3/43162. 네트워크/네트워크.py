from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    
    def bfs(s):
        q = deque([s])
        
        while q:
            now = q.popleft()
            for next in range(n):
                if visited[next] == 0 and computers[now][next] == 1:
                    q.append(next)
                    visited[next] = 1
        
        
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer
#유니온파인드
# def solution(n, computers):
#     parent = [i for i in range(n)]
#     # print(parent)
#     # find-set
#     def find_set(x):
#         if parent[x] == x:
#             return x

#         # return find_set(parent[x])

#         # 경로 압축
#         parent[x] = find_set(parent[x])
#         return parent[x]


#     # union
#     def union(x, y):
#         # 1. 이미 같은 집합인지 체크
#         x = find_set(x)
#         y = find_set(y)

#         # 대표자가 같으니, 같은 집합이다.
#         if x == y:
#             # print('싸이클 발생')
#             return

#         # 2. 다른 집합이라면, 같은 대표자로 수정
#         if x < y:
#             parent[y] = x
#         else:
#             parent[x] = y
            
#     for i in range(n):
#         for j in range(i+1, n):
#             if computers[i][j]:
#                 union(i, j)
#     # print(parent)\
#     answer = 0
#     for k in range(n):
#         if parent[k] == k:
#             answer += 1
#     return answer