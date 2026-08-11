import math

def solution(n):
    return math.comb(2*n, n) // (n+1)