class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0 ; i < n ; i++){
            if (!visited[i]){
                dfs(computers, visited, i, n);
                answer++;
            }
        }
        return answer;
    }
    
    private void dfs(int[][] computers, boolean[] visited, int node, int l){
        visited[node] = true;
        
        for(int i = 0 ; i < l ; i++){
            if(computers[node][i] == 1 && !visited[i]){
                dfs(computers, visited, i, l);
            }
        }
    }
}