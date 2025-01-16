# 단어순서 뒤집기
import sys
input = sys.stdin.readline

N = int(input())
for tc in range(1, N+1):
    arr = input().rstrip().split(' ')
    print(f'Case #{tc}:', *arr[::-1])