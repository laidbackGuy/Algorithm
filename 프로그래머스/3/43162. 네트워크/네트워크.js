function solution(n, computers) {
    var answer = 0;
    
    const visited = Array(n).fill(false);
    
    const find_network = (s) => {
        visited[s] = true;
        
        let head = 0;
        const q = [s];
        
        while(head < q.length){
            const now = q[head++];
            
            for(let next=0; next<n; next++){
                if(computers[now][next] === 0) continue;
                if(visited[next] === true) continue;
                q.push(next);
                visited[next] = true;
            }
        }
    }
    
    for(let i=0; i<n; i++){
        if(visited[i] === true) continue;
        find_network(i);
        answer++;
    }
    
    return answer;
}