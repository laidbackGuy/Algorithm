# KCPC
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    rank = 1
    n, k, t, m = map(int, input().split())
    table = [[]] + [[0] * (k+1) for _ in range(n)]
    submit = [0] * (n+1)
    last_submit = [0] * (n+1)
    for time in range(m):
        i, j, s = map(int, input().split())
        table[i][j] = max(table[i][j], s)
        submit[i] += 1
        last_submit[i] = time
        
    score = sum(table[t])
    for i in range(1, n+1):
        if i == t:
            continue
        now = sum(table[i])
        if now > score:
            rank += 1
            continue
        if now == score:
            if submit[i] < submit[t]:
                rank += 1
                continue
            elif submit[i] == submit[t]:
                if last_submit[i] < last_submit[t]:
                    rank += 1
                    continue
    print(rank)