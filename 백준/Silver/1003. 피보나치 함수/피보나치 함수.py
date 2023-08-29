# 피보나치 함수
import sys


# def fibo(n):
#     if n == 0:
#         memo[n] = 0
#     elif n == 1:
#         memo[n] = 1
#     else:
#         memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]

def fibo2(n):
    fibo_list = [0] * (n+1)
    fibo_list[0] = 0
    if n >= 1:
        fibo_list[1] = 1
    for i in range(2, n+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list[n]


T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    # memo = [0] * (N + 1)
    # memo[1] = 1
    if N == 0:
        print(1, 0)
    else:
        print(fibo2(N-1), fibo2(N))



