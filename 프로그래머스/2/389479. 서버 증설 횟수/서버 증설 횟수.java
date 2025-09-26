import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int server = 0;
        int[] table = new int[24 + k];
        
        // System.out.println(Arrays.toString(table));
        
        for(int time = 0 ; time < 24 ; time ++){
            int serverDown = table[time];
            if(serverDown > 0){
                server -= serverDown;
            }
            
            int oper = 0;
            int need = players[time] / m;
            if (need > server){
                oper = need - server;
                server += oper;
                table[time + k] += oper;
                answer += oper;
                // System.out.println("oper:" + oper);
                
            }
            // System.out.print(players[time]);
            // System.out.print(server);
            // System.out.println(oper);
            // System.out.println("time:" + time);
            // System.out.println("need:" + need);
            // System.out.println();
        }
        return answer;
    }
}