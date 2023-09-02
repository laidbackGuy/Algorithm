# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

rec, prob = map(int, input().split())
dogam = {}
dogam2 = {}
for i in range(1, rec+1):
    input_str = input().rstrip()
    dogam[i] = input_str
    dogam2[input_str] = i
# print(dogam)
# print(dogam2)
for j in range(prob):
    order = input().rstrip()
    if order.isdigit():
        print(dogam[int(order)])
    else:
        print(dogam2[order])