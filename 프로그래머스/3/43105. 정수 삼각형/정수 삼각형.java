import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int n = triangle.length;
        int[][] dp = new int[n][n];
        
        dp[0][0] = triangle[0][0];
        
        for(int i=1 ; i < n ; i++){
            for(int j=0 ; j <= i ; j++){
                if(j == 0){
                    dp[i][j] = triangle[i][0] + dp[i-1][0];
                }
                else{
                    dp[i][j] = triangle[i][j] + Math.max(dp[i-1][j], dp[i-1][j-1]);
                }
            }
        }
        
        for(int i = 0;i < n;i++){
            if(dp[n-1][i] > answer){
                answer = dp[n-1][i];
            }
        }
        return answer;
    }
}