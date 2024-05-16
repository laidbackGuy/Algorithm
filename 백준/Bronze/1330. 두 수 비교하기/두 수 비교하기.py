A, B = map(int, input().split())
if A > B:
    print('>') # A가 B보다 큰 경우에는 '>'를 출력한다.
elif A < B: 
    print('<') # A가 B보다 작은 경우에는 '<'를 출력한다.
elif A == B:
    print('==') # A와 B가 같은 경우에는 '=='를 출력한다.
