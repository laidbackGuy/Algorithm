def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    cam = routes[0][1]
    
    for ent, ext in routes:
        if ent > cam:
            cam = ext
            answer += 1
    
    return answer