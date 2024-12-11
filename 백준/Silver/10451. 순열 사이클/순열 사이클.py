# 순열 사이클
import sys
input = sys.stdin.readline


def dfs(s):
    global answer
    visited[s] = 1
    now = s
    while 1:
        next = adj[now]
        if visited[next]:
            answer += 1
            return
        visited[next] = 1
        now = next


T = int(input())
for _ in range(T):
    N = int(input())
    adj = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    answer = 0
    for start in range(1, N+1):
        if visited[start] == 0:
            dfs(start)
    print(answer)