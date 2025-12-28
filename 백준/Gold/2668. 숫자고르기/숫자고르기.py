# 숫자고르기
import sys
input = sys.stdin.readline

N = int(input())
adj = [0] * (N+1)
for i in range(1, N+1):
    adj[i] = int(input())

visited = [0] * (N+1)
res = []
for now in range(1, N+1):
    stack = []
    if visited[now] == 0:
        stack.append(now)
        while 1:
            next = adj[now]
            if visited[next] == 0:
                if next in stack:
                    cycle = stack[stack.index(next):]
                    for num in cycle:
                        visited[num] = 1
                    res += cycle
                    break
                else:
                    stack.append(next)
                    now = next
            else:
                break
res.sort()
print(len(res))
for num in res:
    print(num)