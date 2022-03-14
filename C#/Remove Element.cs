public class Solution27 {
    public int RemoveElement(int[] nums, int val) {
        
        int m = 0;
        
        for(int i=0;i<nums.Length;i++)
        {
            if(nums[i]!=val)
            {
                nums[m] = nums[i];
                m++;
            }
        }
        
        return m;
    }
}