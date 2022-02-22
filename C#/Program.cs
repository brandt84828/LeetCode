namespace Algorithms;
class Program
    {
        static void Main(string[] args)	
        {

           string columnTitle = "ZY";
           int ans = 0;

           foreach(char c in columnTitle)
           {
               int d = c - 'A' + 1;

               ans = ans * 26 + d;
           }

           Console.WriteLine(ans);
        }
    }