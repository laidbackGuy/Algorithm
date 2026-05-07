function solution(numbers, target) {
    var answer = 0;
    
    const rec = (cur, cnt) => {
        if (cnt === numbers.length){
            if (cur === target){
                answer++;
            }
            return;
        }
        rec(cur - numbers[cnt], cnt + 1);
        rec(cur + numbers[cnt], cnt + 1);
    }
    
    rec(0, 0);
    
    return answer;
}