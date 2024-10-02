# Ezreal 여눈부터 가네 ㅈㅈ
from itertools import product
import sys
sys.setrecursionlimit(2500)
N = int(input())

# 직접 구현해서 규칙 찾기
# candis = list(product('15', repeat=N))
# answer = 0
# print(candis)
# for candi in candis:
#     if candi[-1] != '1':
#         now = int(''.join(candi))
#         if now % 15 == 0:
#             answer += 1
#

dp = [0] * 1516
dp[2] = 1
dp[3] = 1

# for문으로 배열 채워버리는 방식
# for i in range(4, 1516):
#     if i % 2 == 0:
#         dp[i] = dp[i-1]*2 + 1
#     else:
#         dp[i] = dp[i-1]*2 - 1


# 재귀로 구현(이게 메모리, 속도면에서 모두 뛰어남)
def ddp(n):
    if n <= 3:
        return dp[n]

    if n % 2 == 0:
        return ddp(n-1) * 2 + 1
    else:
        return ddp(n-1) * 2 - 1


answer = ddp(N)
answer %= 1000000007
# answer = dp[N] % 1000000007
print(answer)