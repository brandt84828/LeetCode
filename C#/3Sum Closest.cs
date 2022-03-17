public class Solution16 {
    public int ThreeSumClosest(int[] nums, int target) {
        int result = nums[0] + nums[1] + nums[nums.Length - 1];
        Array.Sort(nums);
        for (int i = 0; i < nums.Length - 2; i++) {
            int start = i + 1, end = nums.Length - 1;
            while (start < end) {
                int sum = nums[i] + nums[start] + nums[end];
                if (sum > target) {
                    end--;
                } else {
                    start++;
                }
                if (Math.Abs(sum - target) < Math.Abs(result - target)) {
                    result = sum;
                }
            }
        }
        return result;
    }
}