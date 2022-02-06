public class Solution53 {
    public int MaxSubArray(int[] nums) {
        int res = nums[0];
        int curr = nums[0];
        for(int i = 1; i < nums.Length; i++) {
            curr += nums[i];
            if (curr < 0 || nums[i] > curr)
                curr = nums[i];
            if (res < curr)
                res = curr;
        }
        return res;  
    }
}