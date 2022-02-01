public class Solution217 {
    public bool ContainsDuplicate(int[] nums) {
        
        HashSet<int> newArr = new HashSet<int>(nums);
        
        if(newArr.Count<nums.Length)
        {
            return true;
        }
        else
        {
            return false;
        }
        
        
    }
}