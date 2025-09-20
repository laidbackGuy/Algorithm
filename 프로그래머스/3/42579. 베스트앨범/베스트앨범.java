import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<String, ArrayList<int[]>> myMap = new HashMap<>();
        HashMap<String, Integer> genreMap= new HashMap<>();
        
        for(int i = 0 ; i < genres.length ; i++){
            genreMap.putIfAbsent(genres[i], 0);
            int now = genreMap.get(genres[i]);
            genreMap.put(genres[i], now + plays[i]);
            
            myMap.putIfAbsent(genres[i], new ArrayList<int[]>());
            myMap.get(genres[i]).add(new int[]{i, plays[i]});
        }

        myMap.forEach((genre, songList) -> {
            songList.sort((a, b) -> {
                // 1. 재생수(a[1], b[1]) 기준 내림차순
                if (a[1] == b[1]) {
                    // 2. 재생수가 같으면 고유번호(a[0], b[0]) 기준 오름차순
                    return a[0] - b[0];
                }
                return b[1] - a[1];
            });
        });
        
        List<String> orderedGenres = new ArrayList<>(genreMap.keySet());
        orderedGenres.sort((genre1, genre2) -> 
            genreMap.get(genre2) - genreMap.get(genre1));
        
        for(String genre : orderedGenres){
            ArrayList<int[]> songList = myMap.get(genre);
            if(songList.size() > 1){
                for(int i = 0 ; i < 2 ; i++){
                    int[] song = songList.get(i);
                    answer.add(song[0]);
                }
            }
            else{
                int[] song = songList.get(0);
                answer.add(song[0]);
            }
        }
        System.out.println(answer);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}