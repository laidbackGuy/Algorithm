function solution(n, edge) {
    var answer = 0;
    const adj = Array.from({length:n+1}, () => []);
    for(const [u, v] of edge){
        adj[u].push(v);
        adj[v].push(u);
    }
    let farest = 0;
    let cnt = 0;
    
    const visited = Array(n+1).fill(-1);

    const q = [];
    let head = 0;
    
    q.push(1);
    visited[1] = 0
    
    while(head < q.length){
        const now = q[head++];
        const dist = visited[now];
        
        for(next of adj[now]){
            if (visited[next] >= 0){
                continue;
            }
            visited[next] = dist + 1;

            if (dist + 1 > farest){
                farest = dist + 1;
                cnt = 1;
            }
            else if (dist + 1 === farest){
                cnt++;
            }
            q.push(next);
        }
    }
    
    return cnt;
}