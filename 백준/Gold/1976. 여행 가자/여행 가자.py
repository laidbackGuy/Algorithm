# 여행 가자
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


N = int(input())
M = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
path = list(map(int, input().split()))

# union-find를 쓰기 위해 각자를 부모로 지정하고 시작
parents = [i for i in range(N)]
# print(parents)
for i in range(N):
    for j in range(N):
        if adj[i][j]:
            if find_set(i) != find_set(j):
                union(i, j)
# print(parents)
path_parents = []
for i in path:
    path_parents.append(parents[i-1])   # 여행지는 1부터시작하기 때문에 -1 해주기 

if len(set(path_parents)) == 1:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)