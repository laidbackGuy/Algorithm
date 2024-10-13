def solution(skill, skill_trees):
    answer = 0
    N = len(skill)
    
    for tree in skill_trees:
        check = [0] * N
        check[0] = 1
        for c in tree:
            if c not in skill:
                continue
            else:
                idx = None
                for i in range(N):
                    if c == skill[i]:
                        idx = i
                if check[idx] != 1:
                    break
                else:
                    check[idx] = 0
                    if idx != N-1:
                        check[idx+1] = 1
        else:
            answer += 1
    return answer