function solution(signals) {
    var answer = 0;
    
    let limit = 1;
    
    for([g, y, r] of signals){
        limit *= (g + y + r);
    }
    
    for(let time = 1; time < limit; time++){
        let flag = true;
        for([g, y, r] of signals){
            if((g+1 > time % (g+y+r)) || (time % (g+y+r) > g+y)){
                flag = false;
                break;                
            }    
        }
        if(flag) return time;
    }
    
    return -1;
}