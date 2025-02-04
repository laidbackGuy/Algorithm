# 걷기
import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())
if X == 0 and Y == 0:
    answer = 0
elif X == 0 and Y != 0:
    if W < S:
        answer = W * Y
    else:
        if Y % 2 == 0:
            answer = S * Y
        else:
            answer = S*(Y-1) + W
elif X != 0 and Y == 0:
    if W < S:
        answer = W * X
    else:
        if X % 2 == 0:
            answer = S * X
        else:
            answer = S*(X-1) + W
else:
    if S < W:
        answer = 0
        if X > Y:
            answer += Y * S
            remain = X - Y
        else:
            answer += X * S
            remain = Y - X
        if remain % 2 == 0:
            answer += remain * S
        else:
            answer += ((remain-1) * S) + W

    elif S > W * 2:
        answer = (X * W) + (Y * W)
    else:
        if X > Y:
            answer = (Y * S) + (X-Y) * W
        else:
            answer = (X * S) + (Y-X) * W
print(answer)