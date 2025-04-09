# NBA 농구
import sys
input = sys.stdin.readline

N = int(input())
answer_A, answer_B = 0, 0
A, B = 0, 0
prev_m, prev_s = 0, 0
winning = None
for _ in range(N):
    team, time = input().rstrip().split()
    min, sec = map(int, time.split(':'))
    # 이기고 있던 시간 계산
    if min == prev_m:
        winning_time = sec - prev_s
    else:
        winning_time = (min - prev_m - 1) * 60 + (60 - prev_s) + sec
        
    # 이기고 있던 시간 계산 만큼 더해주기
    if winning == A:
        answer_A += winning_time
    elif winning == B:
        answer_B += winning_time

    # 득점 더해주기
    if team == '1':
        A += 1
    elif team == '2':
        B += 1

    # 이기고 있는 팀 판별
    if A > B:
        winning = A
        prev_m = min
        prev_s = sec
    elif B > A:
        winning = B
        prev_m = min
        prev_s = sec
    else:
        winning = None
        
# 경기 끝난 후 이긴 시간 계산 후 더해주기
winning_time = (48 - prev_m - 1) * 60 + (60 - prev_s)
if winning == A:
    answer_A += winning_time
elif winning == B:
    answer_B += winning_time

arr = [str(answer_A // 60), str(answer_A % 60), str(answer_B // 60), str(answer_B % 60)]
for i in range(4):
    if len(arr[i]) == 1:
        arr[i] = '0' + arr[i]

print(f'{arr[0]}:{arr[1]}')
print(f'{arr[2]}:{arr[3]}')