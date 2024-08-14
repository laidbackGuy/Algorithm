# 마인크래프트
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

min_spend = 1e9
floor = 0

for target in range(257):
    flag = True
    time = 0
    inven = B
    # print(target)
    for i in range(N):
        for j in range(M):
            now = arr[i][j]
            if now > target:
                time += 2*(now - target)
                if time > min_spend:
                    flag = False
                    break
                inven += (now - target)
            elif now < target:
                time += (target - now)
                if time > min_spend:
                    flag = False
                    break
                inven -= (target - now)
        if flag is False:
            break
    if inven >= 0:
        if time <= min_spend:
            min_spend = time
            floor = target
            # print(target, time, inven)
print(min_spend, floor)

