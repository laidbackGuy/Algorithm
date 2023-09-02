# 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
# print(coins)
used_coin_num = 0
remain_money = K
for coin in coins:
    if remain_money == 0:
        break
    if coin > remain_money:
        continue
    mul_coin = 0
    i = 0
    while True:
        i += 1
        mul_coin = coin * i
        if mul_coin > remain_money:
            i -= 1
            break
    remain_money -= coin * i
    used_coin_num += i
print(used_coin_num)

