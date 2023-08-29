# 경로 찾기

def check_can_go(start, goal):
    stack = []
    visited = [0] * V
    n = start
    while True:
        for w in range(V):
            if adj_m[n][w] and visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                if n == goal:
                    return 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return 0


V = int(input())
adj_m = [list(map(int, input().split())) for _ in range(V)]
can_go_list = [[0] * V for _ in range(V)]

for i in range(V):
    for j in range(V):
        can_go_list[i][j] = check_can_go(i, j)
for row in can_go_list:
    print(*row)

