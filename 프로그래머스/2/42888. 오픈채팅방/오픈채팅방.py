def solution(record):
    answer = []
    id_nick = {}
    for od in record:
        spl = od.split(' ')
        uid = spl[1]
        if spl[0] == 'Enter':
            answer.append([uid, 'Enter'])
            id_nick[uid] = spl[2]
        elif spl[0] == 'Leave':
            answer.append([uid, 'Leave'])
        else:
            id_nick[uid] = spl[2]
    
    # print(id_nick)
    # print(answer)
    for i in range(len(answer)):
        if answer[i][1] == 'Enter':
            answer[i] = f'{id_nick[answer[i][0]]}님이 들어왔습니다.'
        else:
            answer[i] = f'{id_nick[answer[i][0]]}님이 나갔습니다.'
    return answer