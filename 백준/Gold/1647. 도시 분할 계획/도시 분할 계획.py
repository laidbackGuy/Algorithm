import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge = []
for i in range(M):
    A, B, w = map(int, input().split())
    edge.append([A, B, w])
# w를 기준으로 정렬
edge.sort(key=lambda x: x[2])
# print(edge)

# 사이클 발생 여부를 union find로 해결
parents = [0] + [i for i in range(1, N + 1)]


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


# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
for f, t, w in edge:
    # 싸이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # MST 구성이 끝나면
        if N-2 == 0:
            sum_weight = 0
            break
        if cnt == N-2:
            break
# print(parents)
print(sum_weight)
