public class Solution202 {
    public bool IsHappy(int n) {
        
        HashSet<int> set = new HashSet<int>();

        while(n!=1)
        {
            int tmp = n;
            int sum = 0;

            while(tmp>0)
            {
                int digit = tmp % 10;
                sum = sum + digit * digit;
                tmp = tmp / 10;
            }

            n = sum;

            if(set.Contains(n))
            {
                return false;
            }
            else
            {
                set.Add(n);
            }
        }
        
        return true;
    }
}