public class Solution1 {
    public int[] TwoSum(int[] nums, int target) {
        
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for(int i=0;i<nums.Length;i++)
        {
            dict.Add(nums[i],i);
        }
        
        for(int i=0;i<nums.Length;i++)
        {
            int find = target - nums[i];
            
            if(dict.ContainsKey(find) && dict[find]!=i)
            {
                return new int[]{i,dict[find]};
            }
        }
        
        return null;
        
    }
}

/*
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        Dictionary<int, int> dict = new Dictionary<int, int>();
        
        for(int i=0;i<nums.Length;i++)
        {
            
            if(dict.ContainsKey(target - nums[i]))
            {
                return new int[]{i,dict[target - nums[i]]};
            }
            else if(!dict.ContainsKey(nums[i]))
            {
                dict.Add(nums[i],i);
            }
        }
        
        return null;
        
    }
}

*/