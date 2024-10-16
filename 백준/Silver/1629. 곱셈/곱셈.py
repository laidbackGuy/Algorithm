# 곱셈

a, b, c = map(int, input().split())


def solve(A, B, C):
    if B == 1:
        return A % C
    else:
        k = solve(A, B//2, C)
        if B % 2 == 0:
            return (k * k) % C
        else:
            return (k * k * A) % C


print(solve(a, b, c))