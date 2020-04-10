import java.util.*;

public class FirstUniqueCharacter {
    public static void main(String[] args) {
        String s = "loveleetcode";
        Map<Character,Integer> count = new HashMap<>();
        char arr[] = s.toCharArray();
        int ans = -1;

        for(char ch:arr){
            if(!count.containsKey(ch)){
                count.put(ch,0);
            }
            else {
                count.put(ch,count.get(ch)+1);
            }
        }

        for(int i = 0;i<s.length();i++){
            if(count.get(arr[i])==0){
                ans = i;
                break;
            }
        }
        System.out.print(ans);




    }
}
