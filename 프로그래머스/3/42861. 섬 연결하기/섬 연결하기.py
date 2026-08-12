def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    parent = list(range(n))
    # print(parent)
    
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    
    def union(x, y):
        x = find(x)
        y = find(y)
        
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
        
        
    for u, v, cost in costs:
        if find(u) != find(v):
            union(u, v)
            answer += cost
        
        
    return answer