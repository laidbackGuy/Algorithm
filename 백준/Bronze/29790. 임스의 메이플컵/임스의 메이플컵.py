# 임스의 메이플 컵
N, U, L = map(int, input().split())
if N >= 1000:
    res = 'Good'
    if U >= 8000 or L >= 260:
        res = 'Very Good'
else:
    res = 'Bad'
print(res)