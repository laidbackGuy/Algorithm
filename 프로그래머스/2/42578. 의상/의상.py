def solution(clothes):
    my_dict = {}
    for item, category in clothes:
        my_dict.setdefault(category, [])
        my_dict[category].append(item)
    answer = 1
    for v in my_dict.values():
        answer *= (len(v)  + 1)
    return answer - 1