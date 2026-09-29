import java.util.*;


class Solution {
    
    int n;
    int m;
    int[][] visited;
    int[][] maps;
    int answer;
    
    int[] di = {0, 0, 1, -1};
    int[] dj = {1, -1, 0, 0};
    
    
    public int solution(int[][] maps) {
        
        n = maps.length;
        m = maps[0].length;
        visited = new int[n][m];
        this.maps = maps;
        answer = -1;
        
        bfs(0, 0);
        
        return answer;
    }
    
    
    void bfs(int si, int sj){
        Queue<int[]> q = new ArrayDeque<>();
        
        q.offer(new int[]{si, sj});
        visited[si][sj] = 1;
        
        while (!q.isEmpty()){
            int[] cur = q.poll();
            
            int i = cur[0];
            int j = cur[1];
            
            if (i == n-1 && j == m-1){
                answer = visited[i][j];
                break;
            }
            
            for (int k=0; k<4; k++){
                int ni = i + di[k];
                int nj = j + dj[k];
                
                if (ni < 0 || ni >= n || nj < 0 || nj >= m){
                    continue;
                }
                
                if (maps[ni][nj] == 1 && visited[ni][nj] == 0){
                    q.offer(new int[]{ni, nj});
                    visited[ni][nj] = visited[i][j] + 1;
                }
            }
        }
    }
}