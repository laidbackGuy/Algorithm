# 트리의 부모 찾기
def dfs(s):
    stack = []
    n = s
    visited[n] = 1
    while True:
        for w in adj_l[n]:
            if not visited[w]:
                stack.append(n)
                n = w
                visited[n] = stack[-1]
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break


V = int(input())
adj_l = [[] for _ in range(V+1)]
for _ in range(V-1):
    v1, v2 = map(int, input().split())
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

# print(adj_l)
visited = [0] * (V+1)
dfs(1)
# print(visited)
for i in range(2, V+1):
    print(visited[i])
