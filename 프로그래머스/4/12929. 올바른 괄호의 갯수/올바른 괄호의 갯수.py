import math

def solution(n):
    answer = 0
    return math.comb(2*n, n) // (n+1)