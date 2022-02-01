public class Solution28 {
    public int StrStr(string haystack, string needle) {
        
        if(needle.Length==0) return 0;
        
        for(int i=0;i<=haystack.Length-needle.Length;i++)
       {
           int count = 0;

           for(int j=0;j<needle.Length;j++)
           {
               if(haystack[i+j]==needle[j])
               {
                   count++;
               }
               else
               {
                   break;
               }
           }

           if(count==needle.Length)
           {
               return i;
           }

       }
        
        return -1;
        
    }
}