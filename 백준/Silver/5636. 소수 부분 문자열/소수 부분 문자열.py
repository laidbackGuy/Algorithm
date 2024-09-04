# 소수 부분 문자열

import sys
input = sys.stdin.readline

while 1:
    my_str = input().rstrip()
    if my_str == '0':
        break

    if len(my_str) > 5:
        max_range = 5
    else:
        max_range = len(my_str)

    candi = 0
    for ran in range(1, max_range+1):
        for i in range(len(my_str)-ran):
            now = my_str[i:i+ran]
            for j in range(2, int(now)):
                if int(now) % j == 0:
                    break
            else:
                candi = max(int(now), candi)
    print(candi)