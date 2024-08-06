# 너의 평점은
table = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F': 0}

total_point = 0
total_hak = 0
for _ in range(20):
    sub, hak, point = input().split()
    if point == 'P':
        continue
    else:
        total_point += (float(hak) * table[point])
        total_hak += float(hak)

print(total_point / total_hak)