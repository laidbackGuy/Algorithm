def solution(friends, gifts):
    N = len(friends)
    friends_dict = {}
    ans_dict = {}
    
    arr = [[0] * N for _ in range(N)]
    
    gift_points = {}
    
    for i in range(len(friends)):
        gift_points.setdefault(friends[i], 0)
        ans_dict.setdefault(friends[i], 0)
        friends_dict.setdefault(friends[i], i)
        
        
    for gift in gifts:
        history = gift.split(' ')
        arr[friends_dict[history[0]]][friends_dict[history[1]]] += 1
        gift_points[history[0]] += 1
        gift_points[history[1]] -= 1
    
    for i in range(N):
        for j in range(N):
            if i != j:
                if arr[i][j] > arr[j][i]:
                    ans_dict[friends[i]] += 1
                elif arr[i][j] < arr[j][i]:
                    ans_dict[friends[j]] += 1
                elif arr[i][j] == arr[j][i]:
                    if gift_points[friends[i]] > gift_points[friends[j]]:
                        ans_dict[friends[i]] += 1
                    elif gift_points[friends[i]] < gift_points[friends[j]]:
                        ans_dict[friends[j]] += 1
    print(ans_dict)    
    
    max_v = 0
    for k, v in ans_dict.items():
        if v > max_v:
            max_v = v
        
    return max_v / 2
    # print(friends_dict)
    # print(arr)
    # print(gift_points)
    # print(ans_dict)