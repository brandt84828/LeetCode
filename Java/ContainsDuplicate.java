import java.util.*;
public class ContainsDuplicate {
    public static void main(String[] args) {
        int nums[] = {1,1,1,3,3,4,3,2,4,2};
        Map<Integer,Integer> contain = new HashMap<Integer,Integer>();
        for(int num:nums){

            if(contain.containsKey(num)){
                System.out.print(true);
            }
            else {
                contain.put(num,0);
            }
        }

    }
}

/* 使用set不重複的特性
class Solution {
public boolean containsDuplicate(int[] nums) {
        HashSet h=new HashSet<>();
        for(int i=0;i<nums.length;i++){
        h.add(nums[i]);
        }
        if(h.size()<nums.length){
        return true;
        }
        return false;
        }
        }
        */