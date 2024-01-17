def solution(s):
    answer = ''
    array = s.split(' ')
    new_array = []
    for i in range(len(array)):
        array[i] = int(array[i]) 
        
    array.sort()
    answer = str(array[0]) + ' ' + str(array[-1])
    return answer