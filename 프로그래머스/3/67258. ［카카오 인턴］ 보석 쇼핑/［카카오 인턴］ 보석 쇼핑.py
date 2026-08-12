def solution(gems):
    answer = []
    type_cnt = len(set(gems))
    n = len(gems)
    
    min_left, min_right = None, None
    min_length = 100000
    
    table = {}
    left, right = 0, 0
    table[gems[0]] = 1
    cnt = 1
    while 1:
        # 모든 보석 종류를 포함하고 있다면
        if cnt == type_cnt:
            # 현재 길이 측정 및 최소 길이 갱신, 시작과 끝 진열대 번호 기록
            length = right - left
            if length < min_length:
                min_length = length
                min_left, min_right = left, right
            left_gem = gems[left]
            table[left_gem] -= 1
            if table[left_gem] == 0:
                cnt -= 1
            left += 1
        # 모든 보석 종류를 포함하고 있지 않다면
        else:
            right += 1
            if right == n:
                break
            right_gem = gems[right]
            table.setdefault(right_gem, 0)
            table[right_gem] += 1
            if table[right_gem] == 1:
                cnt += 1
    

    return [min_left + 1, min_right + 1]