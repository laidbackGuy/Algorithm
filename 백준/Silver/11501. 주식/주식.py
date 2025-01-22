# 주식
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    chart = list(map(int, input().split()))

    asset = 0
    peak = chart[-1]
    for i in range(N-1, -1, -1):
        if chart[i] > peak:
            peak = chart[i]
        else:
            asset += (peak - chart[i])
    print(asset)