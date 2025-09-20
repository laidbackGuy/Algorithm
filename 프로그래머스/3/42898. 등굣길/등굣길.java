import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m];
        int MOD = 1000000007;

        // 웅덩이를 -1로 먼저 표시
        for (int[] puddle : puddles) {
            dp[puddle[1] - 1][puddle[0] - 1] = -1;
        }

        // 시작점 초기화
        dp[0][0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                
                // 현재 칸이 웅덩이라면 경로 수를 0으로 만들고 건너뜀
                if (dp[i][j] == -1) {
                    dp[i][j] = 0;
                    continue;
                }

                // 위쪽에서 오는 경우의 수 더하기
                if (i > 0) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD;
                }
                
                // 왼쪽에서 오는 경우의 수 더하기
                if (j > 0) {
                    dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD;
                }
            }
        }
        
        return dp[n - 1][m - 1];
    }
}