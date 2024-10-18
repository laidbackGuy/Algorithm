# 후보 추천하기

N = int(input())
K = int(input())
recs = list(map(int, input().split()))
candis = []
points = {}
for rec in recs:
    if rec in candis:
        points[rec] += 1
    elif len(candis) < N:
        candis.append(rec)
        points[rec] = 1
    else:
        min_idx = None
        min_candi = None
        min_v = 1e9
        for i in range(N):
            if points[candis[i]] < min_v:
                min_v = points[candis[i]]
                min_candi = candis[i]
                min_idx = i
        candis.pop(min_idx)
        points[min_candi] = 0
        candis.append(rec)
        points[rec] = 1
candis.sort()
print(*candis)
