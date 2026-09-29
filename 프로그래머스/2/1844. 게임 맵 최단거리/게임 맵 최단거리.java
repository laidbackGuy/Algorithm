import java.util.*;

class Solution {
    
    int n;
    int m;
    int answer;
    int[][] visited;
    int[][] maps;
    
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    
    public int solution(int[][] maps) {
        answer = -1;
        this.maps = maps;
        n = maps.length;
        m = maps[0].length;
        visited = new int[n][m];
        
        bfs(0, 0);
        
        // for (int i = 0; i < visited.length; i++) {
        //     for (int j = 0; j < visited[i].length; j++) {
        //         System.out.print(visited[i][j] + " ");
        //     }
        //     System.out.println();
        // }   
        
        return answer;
    }
    
    void bfs(int si, int sj){
            
            
            Queue<int[]> q = new ArrayDeque<>();
            
            q.offer(new int[]{si, sj});
            visited[0][0] = 1;
            
            while (!q.isEmpty()){
                int[] cur = q.poll();
                int i = cur[0];
                int j = cur[1];
                
                if (i == n-1 && j == m-1){
                    answer = visited[i][j];
                    break;
                }
                
                for (int k=0; k<4; k++){
                    int ni = i + dx[k];
                    int nj = j + dy[k];
                    
                    if (ni < 0 || ni >= n || nj < 0 || nj >= m){
                        continue;
                    } 
                    
                    if (maps[ni][nj] == 1 && visited[ni][nj] == 0){
                        visited[ni][nj] = visited[i][j] + 1;
                        q.offer(new int[]{ni, nj});
                    }
                }
                
            }
            
        }
}