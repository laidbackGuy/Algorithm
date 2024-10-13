def solution(s):
    answer = ''
    flag = True
    for c in s:
        if c == ' ':
            flag = True
            answer += c
        else:
            if flag:
                if c.isalpha():
                    answer += c.upper()
                else:
                    answer += c
            else:
                answer += c.lower()
            flag = False
    
#         if not word:
#             answer += ' '
#             continue
#         if word[0].isalpha():
#             answer += word[0].upper()
#         else:
#             answer += word[0]
#         if len(word) > 1:
#             for i in range(1, len(word)):
#                 answer += word[i].lower()
                    
#         answer += ' '
    return answer