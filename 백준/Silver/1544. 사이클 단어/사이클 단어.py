# 사이클 단어
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
word_list = []
for _ in range(N):
    now = input().rstrip()
    if not word_list:
        word_list.append(now)
    else:
        M = len(now)
        flag = False
        for word in word_list:
            if len(word) == M:
                now_word = deque(list(now))
                for _ in range(M):
                    if ''.join(now_word) == word:
                        flag = True
                        break
                    now_word.append(now_word.popleft())
        if not flag:
            word_list.append(now)
print(len(word_list))

