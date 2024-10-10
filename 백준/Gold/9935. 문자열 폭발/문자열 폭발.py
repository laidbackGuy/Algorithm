# 문자열 폭발
import sys
input = sys.stdin.readline

my_str = input().rstrip()
explode_str = input().rstrip()
length = len(explode_str)
stack = []
last_c = explode_str[-1]

for c in my_str:
    stack.append(c)
    if c == last_c:
        if ''.join(stack[len(stack) - length:]) == explode_str:
            for _ in range(length):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
