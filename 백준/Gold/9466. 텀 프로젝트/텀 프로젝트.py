# 텀 프로젝트
import sys
input = sys.stdin.readline


def check(idx):
    global answer
    now = idx
    cycle = []
    while 1:
        visited[now] = 1
        cycle.append(now)
        next = adj[now]
        if visited[next] == 1:
            if next in cycle:
                answer -= (len(cycle) - cycle.index(next))
            return
        now = next


T = int(input())
for tc in range(T):
    N = int(input())
    answer = N
    adj = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)

    for i in range(1, N+1):
        if visited[i] == 0:
            check(i)

    print(answer)