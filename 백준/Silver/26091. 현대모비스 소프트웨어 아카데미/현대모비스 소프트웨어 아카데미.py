# 현대모비스 소프트웨어 아카데미
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
# print(arr)
left = 0
right = N-1
answer = 0
# print(left, right)

flag = True
if left == right:
    answer = 0
    flag = False
if flag is True:
    while 1:
        if arr[left] + arr[right] >= M:
            answer += 1
            left += 1
            right -= 1
            if left >= right:
                break
        else:
            new_left = left
            left_flag = None
            while left < right:
                new_left += 1
                if new_left == right:
                    left_flag = False
                    break
                if arr[new_left] != arr[left]:
                    left_flag = True
                    break
            new_right = right
            right_flag = None
            while 1:
                new_right -= 1
                if new_right == left:
                    right_flag = False
                    break
                if arr[new_right] != arr[right]:
                    left_flag = True
                    break
            if left_flag and right_flag:
                dif_left = arr[new_left] - arr[left]
                dif_right = arr[right] - arr[new_right]
                if dif_left <= dif_right:
                    left = new_left
                    if left >= right:
                        break
                else:
                    right = new_right
                    if left >= right:
                        break
            else:
                if left_flag and not right_flag:
                    left = new_left
                    if left >= right:
                        break
                elif right_flag and not left_flag:
                    right = new_right
                    if left >= right:
                        break
                else:
                    break
        # print(left, right)

print(answer)

# 3 3 5 5 6 7