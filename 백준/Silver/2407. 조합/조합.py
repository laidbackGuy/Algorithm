# 조합
N, M = map(int, input().split())

N_fac = 1
for i in range(1, N+1):
    N_fac *= i

M_fac = 1
for j in range(1, M+1):
    M_fac *= j

NM_fac = 1
for k in range(1, N-M+1):
    NM_fac *= k

# print(N_fac, M_fac, NM_fac)
ans = N_fac // (M_fac * NM_fac)
print(ans)
