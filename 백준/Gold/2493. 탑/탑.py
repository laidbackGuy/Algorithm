N = int(input())
if N == 1:
    print(0)
else:
    towers = list(map(int, input().split()))
    table = [0] * N
    stack = [(towers[N-1], N-1)]
    for i in range(N-2, -1, -1):
        height = towers[i]
        while stack:
            now, idx = stack[-1]
            if now <= height:
                stack.pop()
                table[idx] = i + 1
            else:
                break
        stack.append((towers[i], i))
    print(*table)