import java.util.*;
public class CountingElements {
    public static void main(String[] args) {
        int arr[] = {1,1,2,2};
        Map<Integer,Integer> ans = new HashMap<>();
        int count = 0;

        for(int i = 0;i<=1000;i++){
            ans.put(i,0);
        }

        for(int num:arr){
            ans.put(num,ans.get(num)+1);
        }


        for(int i = 0;i<1000;i++){ //要記得最後一位數，因為到1000
            if(ans.get(i)>0&&ans.get(i+1)>0){
                count = count + ans.get(i);
            }

        }

        System.out.print(count);
    }
}