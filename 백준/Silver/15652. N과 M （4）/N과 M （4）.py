# N과 M (4)

n, m = map(int, input().split())


def p(cur, my_list, cnt):
    if cnt == m:
        print(*my_list)
        return

    for num in range(cur, n+1):
        my_list.append(num)
        p(num, my_list, cnt + 1)
        my_list.pop()


p(1, [], 0)