function solution(brown, yellow) {
    if ((yellow * 2) + 6 === brown){
        return [yellow + 2, 3];  
    }
    let h = 2, w = 0;
    
    while(h<1500){
        if (yellow % h === 0){
            w = yellow / h;
            if (((w*2) + (h+2)*2) === brown){
                return [w+2, h+2]
            }
        } 
        h++;
    }
}