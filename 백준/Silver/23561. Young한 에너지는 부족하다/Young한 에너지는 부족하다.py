import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = arr[2*N-1] - arr[N]
print(answer)