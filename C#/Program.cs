namespace Algorithms;
class Program
    {
        static void Main(string[] args)	
        {

           string haystack = "hello";
           string needle = "ll";

           for(int i=0;i<haystack.Length-needle.Length;i++)
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
        }
    }