def solution(players, m, k):
    answer = 0
    table = [0] * (24+k)
    server = 0
    for i in range(24):
        server_down = table[i]
        if server_down:
            server -= server_down
        
        need = players[i] // m
        if need > server:
            server_on = need - server
            answer += server_on
            server += server_on
            table[i+k] += server_on

    return answer