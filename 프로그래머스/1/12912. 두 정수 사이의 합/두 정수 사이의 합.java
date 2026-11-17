import java.util.*;


class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        
        int l = 0;
        int r = 0;

        if (a > b) {
            l = b;
            r = a;
        } else if (a < b) {
            l = a;
            r = b;
        } else {
            return a;
        }

        System.out.println(l);
        System.out.println(r);

        for (int i = l; i <= r; i++) {
            answer += i;
        }

        return answer;
    }
}