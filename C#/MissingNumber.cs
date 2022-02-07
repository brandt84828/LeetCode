public class Solution268 {
    public int MissingNumber(int[] nums) {
        int total = 0;
        int temp = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            total = total + (i+1);
            temp = temp + nums[i];
        }
        
        return total-temp;
    }
}