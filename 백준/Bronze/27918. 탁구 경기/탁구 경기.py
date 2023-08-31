N = int(input())
D = 0
P = 0
flag = False
for _ in range(N):
    if input() == 'D':
        D += 1
    else:
        P += 1
    if abs(D-P) == 2:
        flag = True
        print(f'{D}:{P}')
        break
if not flag:
    print(f'{D}:{P}')