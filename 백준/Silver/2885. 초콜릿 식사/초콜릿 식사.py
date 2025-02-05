# 초콜릿 식사
import sys
input = sys.stdin.readline

K = int(input())
min_size = None
flag = False
length = 0
for i in range(21):
    if 1 << i > K:
        min_size = 2**i
        break
    elif 1 << i == K:
        min_size = 2**i
        flag = True
        break
if not flag:
    b = bin(K)
    length = 1
    space = 0
    for i in range(3, len(b)):
        space += 1
        if b[i] == '1':
            length += space
            space = 0
print(min_size, length)
