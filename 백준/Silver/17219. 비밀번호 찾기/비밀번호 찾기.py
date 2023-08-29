# 비밀번호 찾기
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
site_password = {}
for _ in range(N):
    site, password = input().strip().split()
    site_password[site] = password

for _ in range(M):
    print(site_password[input().strip()])


