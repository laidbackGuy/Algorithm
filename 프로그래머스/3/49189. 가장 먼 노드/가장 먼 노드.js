function solution(n, edge) {
    var answer = 0;
    const adj = Array.from({length:n+1}, () => Array(n+1).fill(0));
    for(const [u, v] of edge){
        adj[u][v] = 1;
        adj[v][u] = 1;
    }
    
    let farest = 0;
    let cnt = 0;
    
    const visited = Array.from({length:n+1}, () => [false, 0]);
    
    const q = [];
    let head = 0;
    
    q.push(1);
    visited[1][0] = true, visited[1][1] = 0;
    console.log()
    while(head < q.length){
        const now = q[head++];
        
        for(let next = 1; next<n+1; next++){
            if (adj[now][next] === 0){
                continue;
            }
            if (visited[next][0] === true){
                continue;
            }
            visited[next][0] = true;
            visited[next][1] = visited[now][1] + 1;
            if (visited[next][1] > farest){
                farest = visited[next][1];
                cnt = 1;
            }
            else if (visited[next][1] === farest){
                cnt++;
            }
            q.push(next);
        }
    }
    
    // console.log(visited);
    return cnt;
}