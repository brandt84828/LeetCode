public class Solution125 {
    public bool IsPalindrome(string s) {
        
        string ss = "";
        
        foreach (var ch in s)
        {
            if ((int)ch <= 57 && (int)ch >= 48)
            {
                ss = ss + ch.ToString().ToLower();
            }
            else if ((int)ch <= 90 && (int)ch >= 65)
            {
                ss = ss + ch.ToString().ToLower();
            }
            else if ((int)ch <= 122 && (int)ch >= 97)
            {
                ss = ss + ch.ToString().ToLower();
            }
            else
            {

            }
        }


        for (int i = 0; i < ss.Length / 2; i++)
        {
            if (ss[i] != ss[ss.Length - 1 - i])
            {
                return false;
            }
        }     
        
        return true;
    }
}