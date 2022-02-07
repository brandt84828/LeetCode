public class Solution26 {
    public int RemoveDuplicates(int[] nums) {
        int curr = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            if(nums[i]!=nums[curr])
            {
                nums[curr+1] = nums[i];
                curr++;
            }
        }
        
        if(nums.Length==0)
        {
            return 0;
        }
        else
        {
            return curr+1;    
        }
        
    }
}