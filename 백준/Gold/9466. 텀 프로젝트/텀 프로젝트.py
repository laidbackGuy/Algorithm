# 텀 프로젝트
import sys
from collections import deque
input = sys.stdin.readline

'''
사이클 여부를 판단하는 로직이 핵심
'''

def dfs(now):
    global answer
    cycle = []
    while 1:
        visited[now] = 1
        cycle.append(now)
        # print(cycle)
        next = adj[now]
        if visited[next] == 1:
            if next in cycle:
                # print('갓챠', next)
                # print(cycle)
                # print(cycle.index(next))
                answer -= (len(cycle) - cycle.index(next))
                # print(answer)
                # print()
            return
        now = next


T = int(input())
for tc in range(T):
    N = int(input())
    answer = N
    adj = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)

    for start in range(1, N+1):
        if visited[start] == 0:
            dfs(start)

    # print(visited)
    print(answer)