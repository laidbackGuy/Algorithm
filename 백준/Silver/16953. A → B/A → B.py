# A -> B

A, B = map(int, input().split())


def find(cur, cnt):
    global answer

    if cur == B:
        answer = cnt
    if cur > B:
        return

    find(cur * 2, cnt + 1)
    find((cur * 10) + 1, cnt + 1)


answer = 0
find(A, 0)
if not answer:
    answer = -2
print(answer + 1)