public class Solution387 {
    public int FirstUniqChar(string s) {
        var count = new int[256];

        foreach (var c in s) {
            count[c]++;
        }

        for(int i=0;i<s.Length;i++)
        {
            if(count[s[i]]==1)
            {
                return i;
            }
        }
        
        return -1;
    }
}