# Ezreal 여눈부터 가네 ㅈㅈ
from itertools import product

N = int(input())
# candis = list(product('15', repeat=N))
# answer = 0
# print(candis)
# for candi in candis:
#     if candi[-1] != '1':
#         now = int(''.join(candi))
#         if now % 15 == 0:
#             answer += 1
#
# print(answer % 1000000007)

dp = [0] * 1516
dp[2] = 1
dp[3] = 1

for i in range(4, 1516):
    if i % 2 == 0:
        dp[i] = dp[i-1]*2 + 1
    else:
        dp[i] = dp[i-1]*2 - 1

answer = dp[N] % 1000000007
print(answer)