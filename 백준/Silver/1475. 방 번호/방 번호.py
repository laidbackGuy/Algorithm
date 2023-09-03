# 방 번호
room_num = input()
num_set = {'0' : 1, '1' : 1, '2' : 1, '3' : 1, '4' : 1, '5' : 1, '6' : 1, '7' : 1, '8' : 1, '9' : 1}
cnt = 1
for num in room_num:
    if num == '6':
        if num_set['6'] == 0:
            if num_set['9'] >= 1:
                num_set['9'] -= 1
            else:
                for i in num_set:
                    num_set[i] += 1
                num_set['6'] -= 1
                cnt += 1
        else:
            num_set['6'] -= 1

    elif num == '9':
        if num_set['9'] == 0:
            if num_set['6'] >= 1:
                num_set['6'] -= 1
            else:
                for i in num_set:
                    num_set[i] += 1
                num_set['9'] -= 1
                cnt += 1
        else:
            num_set['9'] -= 1

    else:
        if num_set[num] >= 1:
            num_set[num] -= 1
        else:
            for i in num_set:
                num_set[i] += 1
            num_set[num] -= 1
            cnt += 1
        # print(num_set)
print(cnt)
