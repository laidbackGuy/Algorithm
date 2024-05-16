while True:
    try:
        for tc in range(20):
            N = int(input())
            tile = [1, 1, 3]
    
            for i in range(3, N+1):
                tile.append(tile[i-1] + tile[i-2]*2)
    
            print(tile[N])
    except:
        break