public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        
        int max = 0;
        int count = 0;
        
        for(int i =0;i<nums.Length;i++)
        {
            if(nums[i]==1)
            {
                count = count + 1;
            }
            else
            {
                count = 0;
            }
            
            if(count>max) max=count;
        }
        
        return max;
        
    }
}