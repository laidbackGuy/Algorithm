# 기술 연계마스터 임스
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
skills = input().rstrip()
L, S = 0, 0
answer = 0
for skill in skills:
    if skill == 'L':
        L += 1
    elif skill == 'S':
        S += 1
    elif skill == 'R':
        if L:
            L -= 1
            answer += 1
        else:
            break
    elif skill == 'K':
        if S:
            S -= 1
            answer += 1
        else:
            break
    else:
        answer += 1
print(answer)

