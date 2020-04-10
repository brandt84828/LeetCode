import java.util.*;
public class MajorityElement {

    public static void main(String[] args) {
        // write your code here
        int  nums[] = {3,2,3};
        Map<Integer,Integer> ans = new HashMap<Integer, Integer>();
        int majorityelement = nums[0];

        for(int num:nums){

            if(!ans.containsKey(num)){
                ans.put(num,1);
            }else{

                ans.put(num,ans.get(num)+1);

            }
        }
        for (Integer key : ans.keySet()) {
            if(ans.get(key)>ans.get(majorityelement)){
                majorityelement = key;
            }
        }


    }
}
