public class Solution171 {
    public int TitleToNumber(string columnTitle) {
    
       int ans = 0;

       foreach(char c in columnTitle)
       {
           int d = c - 'A' + 1;

           ans = ans * 26 + d;
       }
        
        return ans;
    }
}