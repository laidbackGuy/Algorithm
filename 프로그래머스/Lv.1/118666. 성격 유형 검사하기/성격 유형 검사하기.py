def solution(survey, choices):
    answer = ''
    point_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            point_dict[survey[i][0]] += (4 - choices[i])
        elif choices[i] > 4:
            point_dict[survey[i][1]] += (choices[i] - 4)
    # print(point_dict)
    if point_dict['R'] < point_dict['T']:
        answer += 'T'
    else:
        answer += 'R'
    
    if point_dict['C'] < point_dict['F']:
        answer += 'F'
    else:
        answer += 'C'
    
    if point_dict['J'] < point_dict['M']:
        answer += 'M'
    else:
        answer += 'J'
    
    if point_dict['A'] < point_dict['N']:
        answer += 'N'
    else:
        answer += 'A'
        
    return answer