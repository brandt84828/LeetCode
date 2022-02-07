public class Solution283 {
    public void MoveZeroes(int[] nums) {
        int nonZeroCount = 0;

        for(int i=0;i<nums.Length;i++)
        {
            if(nums[i]!=0)
            {
                int temp  = nums[i];
                nums[i] = nums[nonZeroCount];
                nums[nonZeroCount] = temp;

                nonZeroCount++;

            }
        }
        
    }
}