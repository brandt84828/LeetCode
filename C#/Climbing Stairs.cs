public class Solution70 {
    public int ClimbStairs(int n) {
        if(n<=1) return 1;
        
        int pre = 1;
        int curr = 1;
        
        for(int i=2;i<=n;i++)
        {
            int temp = curr;
            curr = pre + curr;
            pre = temp;
        }
        
        return curr;
    }
}