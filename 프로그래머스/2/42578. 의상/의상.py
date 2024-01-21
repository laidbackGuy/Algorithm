def solution(clothes):
    answer = 0
    my_dict = {}
    for item, category in clothes:
        my_dict.setdefault(category, [])
        my_dict[category].append(item)
    # print(my_dict)
    answer = 1
    for k, v in my_dict.items():
        # print(v)
        answer *= (len(v)  + 1)
    return answer - 1