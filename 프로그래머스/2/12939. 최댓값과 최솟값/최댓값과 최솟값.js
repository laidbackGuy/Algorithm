function solution(s) {
    var answer = '';
    // console.log(...s)
    const arr = s.split(' ')
    // console.log(arr)
    const new_arr = arr.map((num) => {
        return Number(num)
    })
    // console.log(new_arr)
    new_arr.sort((a, b) => a - b)
    // console.log(new_arr)
    answer = new_arr[0].toString() + ' ' + new_arr[new_arr.length - 1].toString()
    
    return answer;
}