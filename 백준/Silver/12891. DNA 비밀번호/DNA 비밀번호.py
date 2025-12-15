# DNA 비밀번호
import sys
input = sys.stdin.readline

S, P = map(int, input().split())
dna_str = input().rstrip()
A, C, G, T = map(int, input().split())

my_dict = {'A': 0, 'C': 1, 'G':2, 'T':3}
answer = 0
check = [0] * 4

for i in range(P):
    now = dna_str[i]
    check[my_dict[now]] += 1

if check[0] >= A and check[1] >= C and check[2] >= G and check[3] >= T:
    answer += 1

for i in range(P, S):
    new = dna_str[i]
    out = dna_str[i-P]

    check[my_dict[out]] -= 1
    check[my_dict[new]] += 1

    if check[0] >= A and check[1] >= C and check[2] >= G and check[3] >= T:
        answer += 1

print(answer)