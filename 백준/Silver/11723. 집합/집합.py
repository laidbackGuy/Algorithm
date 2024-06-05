# 집합
import sys
input = sys.stdin.readline

N = int(input())
S = set()
for _ in range(N):
    input_data = input().split()
    # print(input_data)
    if input_data[0][:2] == 'al' or input_data[0][:2] == 'em':
        order = input_data[0]
        if order == 'all':
            S = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
        elif order == 'empty':
            S = set()
    else:
        order = input_data[0]
        num = input_data[1]
        if order == 'add':
            S.add(num)
        elif order == 'remove':
            if num in S:
                S.remove(num)
        elif order == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)
