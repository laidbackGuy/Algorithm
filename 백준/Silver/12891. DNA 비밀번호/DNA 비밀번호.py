# DNA 비밀번호
import sys
input = sys.stdin.readline

S, P = map(int, input().split())
dna_str = input().rstrip()
A, C, G, T = map(int, input().split())

answer = 0

check = [0] * 4

for i in range(P):
    now = dna_str[i]
    if now == 'A':
        check[0] += 1
    elif now == 'C':
        check[1] += 1
    elif now == 'G':
        check[2] += 1
    elif now == 'T':
        check[3] += 1
# print(check)
if check[0] >= A and check[1] >= C and check[2] >= G and check[3] >= T:
    answer += 1

for i in range(P, S):
    new = dna_str[i]
    out = dna_str[i-P]

    if out == 'A':
        check[0] -= 1
    elif out == 'C':
        check[1] -= 1
    elif out == 'G':
        check[2] -= 1
    elif out == 'T':
        check[3] -= 1

    if new == 'A':
        check[0] += 1
    elif new == 'C':
        check[1] += 1
    elif new == 'G':
        check[2] += 1
    elif new == 'T':
        check[3] += 1
    # print(check)
    if check[0] >= A and check[1] >= C and check[2] >= G and check[3] >= T:
        # print(i, check)
        answer += 1

print(answer)