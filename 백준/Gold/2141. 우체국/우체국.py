# 우체국
import sys
input = sys.stdin.readline

'''
왼쪽과 오른쪽의 차이가 최소가 되는 지점
마을 인구 중 절반을 넘어가는 순간이 존재하는 마을
'''
N = int(input())
total = 0
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    total += b
    arr.append((a, b))
if N == 1:
    print(arr[0][0])
else:
    arr.sort()
    if total % 2 == 0:
        half = total // 2
    else:
        half = total // 2 + 1
    
    current = 0
    for i in range(N):
        current += arr[i][1]
        if current >= half:
            print(arr[i][0])
            break