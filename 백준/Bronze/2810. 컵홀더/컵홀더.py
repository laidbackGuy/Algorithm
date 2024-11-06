# 컵 홀더

N = int(input())
info = input()
print(min(N, info.count('S') + info.count('LL') + 1))