T = int(input())
for tc in range(T):
    R, my_str = map(str, input().split())
    Rep = int(R)

    new_str = ''
    for c in my_str:
        new_str += c*Rep

    print(new_str)