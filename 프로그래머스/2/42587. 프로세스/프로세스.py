from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    
    order = 1
    
    while 1:  
        max_v = max(priorities)
        now = priorities.popleft()
        if now < max_v:  # 우선순위가 더 높은 프로세스가 있어서 다시 큐에 넣는 상황
            if location == 0:
                location = len(priorities)
            else:
                location -= 1
            priorities.append(now)
        else:                       # 꺼낸 프로세스 실행
            if location == 0:
                return order
            else:
                location -= 1
                order += 1