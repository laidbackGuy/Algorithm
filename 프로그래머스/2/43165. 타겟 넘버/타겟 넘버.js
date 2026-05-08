function solution(numbers, target) {
    let answer = 0;

    const stack = [[0, 0]]; // [현재합, 인덱스]

    while (stack.length) {
        const [cur, cnt] = stack.pop();

        if (cnt === numbers.length) {
            if (cur === target) {
                answer++;
            }
            continue;
        }

        stack.push([cur - numbers[cnt], cnt + 1]);
        stack.push([cur + numbers[cnt], cnt + 1]);
    }

    return answer;
}