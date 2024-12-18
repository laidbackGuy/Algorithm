# 행렬
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [list(input().rstrip()) for _ in range(N)]
if (N < 3 or M < 3) and A != B:
    print(-1)
else:
    if A == B:
        print(0)
    else:
        flag = False
        answer = 0
        # for r in A:
        #     print(r)
        # print()
        for i in range(N - 2):
            for j in range(M - 2):
                if A[i][j] != B[i][j]:
                    for k in range(i, i+3):
                        for l in range(j, j+3):
                            if A[k][l] == '1':
                                A[k][l] = '0'
                            else:
                                A[k][l] = '1'
                    answer += 1
                if A == B:
                    flag = True
                    break
                # for r in A:
                #     print(r)
                # print()

        if flag:
            print(answer)
        else:
            print(-1)