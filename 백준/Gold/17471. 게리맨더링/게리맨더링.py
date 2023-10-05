# 게리맨더링
import itertools
from collections import deque

def bfs_1(s):
    global sum_dist_1
    queue = deque([s])
    visited_1[s] = 1
    while queue:
        n = queue.popleft()
        sum_dist_1 += populations[n]
        for w in adj[n]:
            if not visited_1[w]:
                queue.append(w)
                visited_1[w] = 1



def bfs_2(s):
    global sum_dist_2
    queue = deque([s])
    visited_2[s] = 1
    while queue:
        n = queue.popleft()
        sum_dist_2 += populations[n]
        for w in adj[n]:
            if not visited_2[w]:
                queue.append(w)
                visited_2[w] = 1



N = int(input())
populations = [0] + list(map(int, input().split()))
# print(populations)
# 연결 리스트 만들어주기
adj = [[]]
for i in range(1, N+1):
    arr = list(map(int, input().split()))
    arr.pop(0)
    adj.append(arr)
# print(adj)

ans = 1e9

for i in range(1, (1<<N)//2):
    sub1 = []
    sub2 = []
    for j in range(N):
        if i&(1<<j):
            sub1.append(j+1)
        else:
            sub2.append(j+1)
    # print(sub1)
    # print(sub2)
    visited_1 = [0] * (N + 1)
    visited_2 = [0] * (N + 1)

    for area_num in sub1:
        visited_2[area_num] = 1
    for area_num in sub2:
        visited_1[area_num] = 1
    sum_dist_1 = 0
    sum_dist_2 = 0

    start_1 = sub1[0]
    start_2 = sub2[0]

    bfs_1(start_1)
    bfs_2(start_2)

    if sum(visited_1) == N and sum(visited_2) == N:
        # print(sub1, visited_1)
        # print(sub2, visited_2)
        # print(sum_dist_1)
        # print(sum_dist_2)
        dif = abs(sum_dist_1 - sum_dist_2)
        if dif < ans:
            ans = dif
if ans == 1e9:
    ans = -1
print(ans)


