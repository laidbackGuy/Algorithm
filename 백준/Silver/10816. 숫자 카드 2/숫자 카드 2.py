# 숫자 카드2
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums_for_count = list(map(int, input().split()))

card_num_dict = {}
for card in cards:
    if card in card_num_dict:
        card_num_dict[card] += 1
    else:
        card_num_dict[card] = 1
# print(card_num_dict)
for num in nums_for_count:
    if num in card_num_dict:
        print(card_num_dict[num], end=' ')
    else:
        print(0, end=' ')