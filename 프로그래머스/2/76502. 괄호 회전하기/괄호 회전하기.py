from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        stack = []
        for c in s:
            if c == ')':
                if not stack or stack[-1] != '(':
                    break
                else:
                    stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    break
                else:
                    stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    break
                else:
                    stack.pop()
            else:
                stack.append(c)
        else:
            if not stack:
                answer += 1   
        s.append(s.popleft())
    
    return answer