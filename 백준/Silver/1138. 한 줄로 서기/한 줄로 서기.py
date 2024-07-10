# 한 줄로 서기
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

line = [0] * N

for i in range(N-1):
    if i == 0:
        line[arr[i]] = i+1
    else:
        if arr[i] > 0:
            k = 0
            cnt = 0
            while 1:
                if line[k] == 0:
                    cnt += 1
                    if cnt == arr[i]:
                        k += 1
                        while 1:
                            if line[k] == 0:
                                line[k] = i+1
                                break
                            k += 1
                        break
                    k += 1
                else:
                    k += 1
        else:
            k = 0
            while 1:
                if line[k] == 0:
                    line[k] = i+1
                    break
                k += 1
for i in range(N):
    if line[i] == 0:
        line[i] = N
print(*line)