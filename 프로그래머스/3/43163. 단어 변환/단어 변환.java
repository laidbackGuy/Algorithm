import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        int n = begin.length();
        Queue<String> q = new ArrayDeque<>();
        Map<String, Integer> visited = new HashMap<>();
        
        q.offer(begin);
        visited.put(begin, 0);
        
        while (!q.isEmpty()) {
            String now = q.poll();
            int dist = visited.get(now);
            
            if (now.equals(target)) {
                return dist;
            }
            for (String word : words) {
                if (visited.containsKey(word)) {
                    continue;
                }
                int cnt = 0;
                for (int i=0; i<n; i++) {
                    if (now.charAt(i) == word.charAt(i)) {
                        cnt++;
                    }
                }
                if (cnt == n-1) {
                    q.offer(word);
                    visited.put(word, dist + 1);
                }
            }
        }
        
        return answer;
    }
}