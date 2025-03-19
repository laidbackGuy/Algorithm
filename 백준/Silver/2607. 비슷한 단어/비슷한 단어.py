# 비슷한 단어
import sys, copy
input = sys.stdin.readline

N = int(input())
my_word = list(input().rstrip())

answer = 0
for _ in range(N-1):
    compare = my_word[:]
    now_word = input().rstrip()
    cnt = 0
    for c in now_word:
        if c in compare:
            compare.remove(c)
        else:
            cnt += 1
    if cnt <= 1 and len(compare) <= 1:
        answer += 1
print(answer)