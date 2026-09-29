import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Boolean> myMap = new HashMap<>();
        
        for (String num : phone_book) {
            myMap.put(num, true);
        }
        
        for (String num : phone_book) {
            for (int i=1; i<num.length(); i++) {
                if (myMap.containsKey(num.substring(0, i))) {
                    return false;
                }
            }  
        }
        
        return answer;
    }
}