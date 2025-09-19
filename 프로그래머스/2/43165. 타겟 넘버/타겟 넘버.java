class Solution {
    int answer = 0;
    public int solution(int[] numbers, int target) {
        int n = numbers.length;
        find(numbers, target, 0, 0, n);
        return answer;
    }
    
    private void find(int[] numbers, int target, int current, int cnt, int limit){
        if (cnt == limit){
            if(current == target){
                answer++;
            }
            return;
        }
        int now = numbers[cnt];
        find(numbers, target, current - now, cnt + 1, limit);
        find(numbers, target, current + now, cnt + 1, limit);
    }
}