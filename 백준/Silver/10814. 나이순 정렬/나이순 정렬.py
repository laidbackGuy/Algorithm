# 나이순 정렬
N = int(input())
member_dict = {}
for i in range(N):
    age, name = input().split()

    member_dict.setdefault(age, [])
    member_dict[age].append(name)
# print(member_dict)  # {'21': ['Junkyu', 'Dohyun'], '20': ['Sunyoung']}

str_ages = list(member_dict.keys())
ages = list(map(int, str_ages))
ages.sort()
# print(ages)

for age in ages:
    for i in range(len(member_dict[str(age)])):
        print(int(age), member_dict[str(age)][i])