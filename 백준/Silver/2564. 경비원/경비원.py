# IM대비1_경비원
garo, sero = map(int, input().split())
num_store = int(input())
stores_side_d = []  # 상점의 동서남북 중 어느쪽인지와 사각형 꼭짓점으로부터의 거리
sum_min_dis = 0     # 경비원과의 최소거리들의 합
for store in range(num_store):  # 상점 사이드와 거리 받아주기
    store_side, store_d = map(int, input().split())     # 상점 사이드, 거리
    stores_side_d.append((store_side, store_d))    # 딕셔너리에 key : 사이드, value : 거리 넣어주기
# print(stores_side_dis)
dong_side, dong_d = map(int, input().split())   # 동근이(경비원)의 사이드와 거리
# print(stores_side_d)
for store_side, store_d in stores_side_d:
    # 동근이와 상점이 남북으로 마주보고 있다면
    if dong_side + store_side == 3:
        root1 = sero + dong_d + store_d     # 서쪽 거쳐가기
        root2 = sero + (garo - dong_d) + (garo - store_d)   # 동쪽 거쳐가기
        sum_min_dis += min(root1, root2)

    # 동서로 마주보고 있다면
    elif dong_side + store_side == 7:
        root1 = garo + dong_d + store_d     # 북쪽 거쳐가기
        root2 = garo + (sero - dong_d) + (sero - store_d)   # 남쪽 거쳐가기
        sum_min_dis += min(root1, root2)

    # 같은 면에 있다면
    elif dong_side == store_side:
        sum_min_dis += abs(dong_d - store_d)

    # 동근이와 상점이 인접한 면에 위치해 있다면
    else:
        if dong_side == 1:   # 동근이가 1사이드에 있을 때
            if store_side == 3:
                sum_min_dis += dong_d + store_d
            elif store_side == 4:
                sum_min_dis += (garo - dong_d) + store_d

        elif dong_side == 2:   # 동근이가 2사이드에 있을 때
            if store_side == 3:
                sum_min_dis += dong_d + (sero - store_d)
            elif store_side == 4:
                sum_min_dis += (garo - dong_d) + (sero - store_d)

        elif dong_side == 3:    # 동근이가 3사이드에 있을 떄
            if store_side == 1:
                sum_min_dis += dong_d + store_d
            elif store_side == 2:
                sum_min_dis += (sero - dong_d) + store_d

        elif dong_side == 4:    # 동근이가 4사이드에 있을 떄
            if store_side == 1:
                sum_min_dis += dong_d + (garo - store_d)
            elif store_side == 2:
                sum_min_dis += (sero - dong_d) + (garo - store_d)
    # print(sum_min_dis)
print(sum_min_dis)
