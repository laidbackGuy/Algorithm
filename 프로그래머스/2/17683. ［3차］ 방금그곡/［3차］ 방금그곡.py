def solution(m, musicinfos):
    answer = ''
    started = ''
    listened = []
    
    for i in range(len(m)):
        if m[i] == '#':
            listened[-1] = listened[-1] + '#'
        else:
            listened.append(m[i])
            
    flag = False
    for music in musicinfos:
        start, end, name, str_melody = music.split(',')  
        melody = []
        for i in range(len(str_melody)):
            if str_melody[i] == '#':
                melody[-1] = melody[-1] + '#'
            else:
                melody.append(str_melody[i])
                
        play_time = (int(end[0:2]) - int(start[0:2]))*60 + (int(end[3:5]) - int(start[3:5]))
        played = ''
        if play_time < len(melody):
            played = melody[0:play_time]
        elif play_time == len(melody):
            played = melody
        else:
            cnt = play_time // len(melody)
            rest = play_time % len(melody)
            played = (melody * cnt) + melody[0:rest]
            
        for i in range(len(played)-len(listened)+1):
            # print(''.join(played[i:i+len(listened)]))
            for j in range(len(listened)):
                # print(i, j)
                if not listened[j] == played[j+i]:
                    break
            else:
                # print('wow')
                flag = True
                # print(name)
                if answer:
                    # print('?')
                    if int(started[0:2]) > int(start[0:2]):
                        answer = name
                        started = start
                    else:  
                        if int(started[3:5]) > int(start[3:5]):
                            answer = name
                            started = start
                else: 
                    # print('tt')
                    # print(name)
                    answer = name
                    started = start
        
    if flag is False:
        return '(None)'
    
    return answer