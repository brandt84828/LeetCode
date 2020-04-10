import java.lang.reflect.Array;
import java.util.*;
public class GroupAnagrams {
    public static void main(String[] args) {
        String strs[] = {"eat","tea","tan","ate","nat","bat"};
        List<List<String>> ans = new ArrayList<List<String>>();
        Map<String,List> dup = new HashMap<>();

        if(strs.length==0){
            System.out.print(ans);
        }

        for(String str:strs){
            char strarr[] = str.toCharArray();
            Arrays.sort(strarr);
            String sortarr = String.valueOf(strarr);

            if(!dup.containsKey(sortarr)){
                List<String> sublist = new ArrayList<>();
                dup.put(sortarr,sublist);
                dup.get(sortarr).add(str);
                ans.add(sublist);
            }else{
                dup.get(sortarr).add(str);

            }

        }

        System.out.print(ans);


    }
}
