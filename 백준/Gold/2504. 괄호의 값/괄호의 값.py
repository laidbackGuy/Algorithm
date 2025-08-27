# 괄호의 값
import sys
input = sys.stdin.readline

par = input().rstrip()
answer = 0

par_list = list(par)
n = len(par)

if n == 1:
    print(0)
else:
    flag = True

    # 짝맞는 괄호를 숫자로 변환
    new_par_list = []
    prev = False
    for i in range(n-1):
        if prev:
            prev = False
            continue
        if par_list[i] == '(' and par_list[i+1] == ')':
            new_par_list.append('2')
            prev = True
        elif par_list[i] == '[' and par_list[i+1] == ']':
            new_par_list.append('3')
            prev = True
        else:
            new_par_list.append(par_list[i])
            prev = False
    if prev is False:
        new_par_list.append(par_list[-1])

    while 1:
        par_list = new_par_list
        N = len(par_list)
        new_par_list = []
        last_i = -1
        
        # 곱셈 계산
        for i in range(1, N-1):
            if par_list[i].isnumeric():
                if par_list[i-1] == '(' and par_list[i+1] == ')':
                    new_par_list += par_list[last_i+1:i-1]
                    new_par_list += [str(int(par_list[i])*2)]
                    last_i = i+1

                if par_list[i-1] == '[' and par_list[i+1] == ']':
                    new_par_list += par_list[last_i + 1:i - 1]
                    new_par_list += [str(int(par_list[i]) * 3)]
                    last_i = i + 1
        if last_i != N-1:
            new_par_list += par_list[last_i + 1 : N]

        # 종료 조건
        if len(new_par_list) == 1:
            break

        # 덧셈 계산
        par_list = new_par_list
        n = len(par_list)
        new_par_list = []
        last_i = -1
        for i in range(n-1):
            if i <= last_i:
                continue
            if par_list[i].isnumeric() and par_list[i+1].isnumeric():
                new_par_list += par_list[last_i+1:i]
                new_par_list += [str(int(par_list[i]) + int(par_list[i+1]))]
                last_i = i+1
        if last_i != n-1:
            new_par_list += par_list[last_i + 1 : n]

        # 종료 조건
        if len(new_par_list) == 1:
            break
        if len(new_par_list) == N:
            flag = False
            break
    if not flag:
        print(0)
    else:
        print(new_par_list[0])
