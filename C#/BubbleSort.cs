public class BubbleSort {
    public int[] SortArray(int[] nums) {
        int temp = 0;
        for(int i=0;i<nums.Length-1;i++)
        {
            for(int j=1;j<nums.Length-i;j++)
            {
                if(nums[j-1]>nums[j])
                {
                    temp = nums[j-1];
                    nums[j-1] = nums[j];
                    nums[j] = temp;
                }

            }
        }
        return nums;
    }
}