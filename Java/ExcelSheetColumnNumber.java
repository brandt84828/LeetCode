import java.util.*;

public class ExcelSheetColumnNumber {
    public static void main(String[] args) {
        String s = "ZY";
        Map<Character,Integer> Eng = new HashMap<Character, Integer>();
        for(int i = 0;i<26;i++){
            int ascii = 65+i;
            char ch = (char)ascii;
            Eng.put(ch,i+1);
        }

        int times = 0;

        char arr[] = s.toCharArray();
        int ans = 0;
        for(int i = s.length()-1;i>=0;i--){
            ans = (int) (ans + Eng.get(arr[i])*Math.pow(26,times));
            times++;

        }
        System.out.print(ans);


    }

}

/* 更優解
class Solution {
    public int titleToNumber(String s) {
        int i = 0;
        int val = 0;
        while(i<s.length()) {
            int temp = (int) s.charAt(i);
            temp = temp-64;
            val = val*26+temp;
            i++;
        }

        return val;
    }
}
 */