# 나의 인생에는 수학과 함께
import sys, copy
input = sys.stdin.readline

N = int(input())
arr = [list(input().split()) for _ in range(N)]
dp_max = [[0] * N for _ in range(N)]
dp_max[0][0] = int(arr[0][0])


def operator(op, now, value):
    if op == '+':
        now += value
    elif op == '-':
        now -= value
    elif op == '*':
        now *= value
    return now


for j in range(2, N, 2):
    op = arr[0][j-1]
    now = dp_max[0][j-2]
    v = int(arr[0][j])
    dp_max[0][j] = operator(op, now, v)
for i in range(2, N, 2):
    op = arr[i-1][0]
    now = dp_max[i-2][0]
    v = int(arr[i][0])
    dp_max[i][0] = operator(op, now, v)

dp_min = copy.deepcopy(dp_max)

for i in range(1, N):
    if i % 2 == 0:  # 짝수 행
        for j in range(2, N, 2):
            if j == 1:
                dp_max[i][j] = max(
                                   operator(arr[i][j - 1], dp_max[i - 1][j - 1], int(arr[i][j])),
                                   operator(arr[i - 1][j], dp_max[i - 1][j - 1], int(arr[i][j])),
                                   operator(arr[i - 1][j], dp_max[i - 2][j], int(arr[i][j])))
                dp_min[i][j] = min(
                                   operator(arr[i][j - 1], dp_min[i - 1][j - 1], int(arr[i][j])),
                                   operator(arr[i - 1][j], dp_min[i - 1][j - 1], int(arr[i][j])),
                                   operator(arr[i - 1][j], dp_min[i - 2][j], int(arr[i][j])))
            else:
                # print(i, j)
                # print(operator(arr[i][j - 1], dp_min[i][j - 2], int(arr[i][j])),
                #                operator(arr[i][j - 1], dp_min[i - 1][j - 1], int(arr[i][j])),
                #                operator(arr[i - 1][j], dp_min[i - 1][j - 1], int(arr[i][j])),
                #                operator(arr[i - 1][j], dp_min[i - 2][j], int(arr[i][j])))
                dp_max[i][j] = max(operator(arr[i][j - 1], dp_max[i][j - 2], int(arr[i][j])),
                                   operator(arr[i][j - 1], dp_max[i - 1][j - 1], int(arr[i][j])),
                                   operator(arr[i - 1][j], dp_max[i - 1][j - 1], int(arr[i][j])),
                                   operator(arr[i - 1][j], dp_max[i - 2][j], int(arr[i][j])))
                dp_min[i][j] = min(operator(arr[i][j - 1], dp_min[i][j - 2], int(arr[i][j])),
                                   operator(arr[i][j - 1], dp_min[i - 1][j - 1], int(arr[i][j])),
                                   operator(arr[i - 1][j], dp_min[i - 1][j - 1], int(arr[i][j])),
                                   operator(arr[i - 1][j], dp_min[i - 2][j], int(arr[i][j])))
    else:   # 홀수 행
        for j in range(1, N, 2):
            if i == 1:
                if j == 1:
                    dp_max[i][j] = max(operator(arr[i][j - 1], dp_max[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_max[i - 1][j - 1], int(arr[i][j])))
                    dp_min[i][j] = min(operator(arr[i][j - 1], dp_min[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_min[i - 1][j - 1], int(arr[i][j])))
                else:
                    dp_max[i][j] = max(operator(arr[i][j - 1], dp_max[i][j - 2], int(arr[i][j])),
                                       operator(arr[i][j - 1], dp_max[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_max[i - 1][j - 1], int(arr[i][j])))
                    dp_min[i][j] = min(operator(arr[i][j - 1], dp_min[i][j - 2], int(arr[i][j])),
                                       operator(arr[i][j - 1], dp_min[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_min[i - 1][j - 1], int(arr[i][j])))
            else:
                if j == 1:
                    dp_max[i][j] = max(operator(arr[i][j - 1], dp_max[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_max[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_max[i - 2][j], int(arr[i][j])))
                    dp_min[i][j] = min(operator(arr[i][j - 1], dp_min[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_min[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_min[i - 2][j], int(arr[i][j])))
                else:
                    dp_max[i][j] = max(operator(arr[i][j - 1], dp_max[i][j - 2], int(arr[i][j])),
                                       operator(arr[i][j - 1], dp_max[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_max[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_max[i - 2][j], int(arr[i][j])))
                    dp_min[i][j] = min(operator(arr[i][j - 1], dp_min[i][j - 2], int(arr[i][j])),
                                       operator(arr[i][j - 1], dp_min[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_min[i - 1][j - 1], int(arr[i][j])),
                                       operator(arr[i - 1][j], dp_min[i - 2][j], int(arr[i][j])))


# for r in dp_max:
#     print(r)
# print()
# for r in dp_min:
#     print(r)
print(dp_max[N-1][N-1], dp_min[N-1][N-1])