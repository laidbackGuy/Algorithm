import java.util.*;


class Solution {
    
    int answer;
    int maxDist;
    int[] visited;
    List<Integer>[] adj;
    
    public int solution(int n, int[][] edge) {
        answer = 1;
        maxDist = 0;
        adj = new ArrayList[n+1];
        visited = new int[n+1];
        
        for (int i=0; i<n+1; i++) {
            adj[i] = new ArrayList<>();
        }
        
        for (int i=0; i<edge.length; i++) {
            adj[edge[i][0]].add(edge[i][1]);
            adj[edge[i][1]].add(edge[i][0]);
        }
        
        find();
        
        // for (int i=0;i<n+1;i++) {
        //     for (int j=0;j<adj[i].size();j++) {
        //         System.out.print(adj[i].get(j) + " ");
        //     }
        //     System.out.println();
        // }
        
        return answer;
    }
    
    void find() {
        Queue<Integer> q = new ArrayDeque<>();
        
        q.offer(1);
        visited[1] = 1;
        
        while (!q.isEmpty()) {
            int now = q.poll();
            
            if (visited[now] > maxDist) {
                maxDist = visited[now];
                answer = 1;
            } else if (visited[now] == maxDist) {
                answer++;
            }
            
            for (int next : adj[now]) {
                if (visited[next] == 0) {
                    q.offer(next);
                    visited[next] = visited[now] + 1;
                }
            }
        }
    }
}