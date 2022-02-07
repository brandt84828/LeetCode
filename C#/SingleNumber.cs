public class Solution136 {
    public int SingleNumber(int[] nums) {
        int ans = 0;

        foreach(int i in nums)
        {
            ans = ans ^ i;
        }
        
        return ans;
    }
}