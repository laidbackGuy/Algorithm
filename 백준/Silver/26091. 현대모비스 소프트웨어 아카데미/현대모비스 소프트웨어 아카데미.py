# 현대모비스 소프트웨어 아카데미
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N-1
answer = 0
flag = True

if left == right:
    answer = 0
    flag = False

# left, right 포인터 바뀔때마다 항상 left가 right보다 크거나 같은지 확인해줌
if flag is True:
    while 1:
        # 왼쪽 오른쪽 더해서 요건 충족하면 팀으로 선발
        # 왼쪽 오른쪽 포인터 한개씩 이동
        if arr[left] + arr[right] >= M:
            answer += 1
            left += 1
            right -= 1
            if left >= right:
                break
        else:
            # 값이 달라질때까지 왼쪽 포인터 옮기기
            left_flag = None
            new_left = left
            while left < right:
                new_left += 1
                if new_left == right:
                    left_flag = False
                    break
                if arr[new_left] != arr[left]:
                    left_flag = True
                    break

            if left_flag:
                left = new_left
            else:
                break

print(answer)