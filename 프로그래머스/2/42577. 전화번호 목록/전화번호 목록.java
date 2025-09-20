import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Boolean> myMap = new HashMap<>();
        
        for(String phone_num : phone_book){
            myMap.put(phone_num, true);
        }
        
        for(String phone_num : phone_book){
            int n = phone_num.length();
            for(int i = 1 ; i < n ; i++){
                if(myMap.containsKey(phone_num.substring(0, i))){
                    return false;
                }
            }
        }
        return true;
    }
}