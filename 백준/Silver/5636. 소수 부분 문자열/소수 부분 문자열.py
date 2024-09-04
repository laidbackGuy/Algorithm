# import sys
# input = sys.stdin.readline.rstrip()
while True:
    n = input()
    if n == '0':
        break
    ans = 0
    for i in range(len(n)+1):
        for j in range(i):
            now = n[j:i]
            now = int(now)
            for k in range(2,now):
                if now%k == 0 or now > 100000:
                    break
            else:
                if ans < int(now):
                    ans = int(now)
    print(ans)
