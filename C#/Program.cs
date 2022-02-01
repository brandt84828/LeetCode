namespace Algorithms;
class Program
    {
        static void Main(string[] args)	
        {

            int[] nums = new int[]{2,4,2,3,5,4,9,8,7};
            HashSet<int> set = new HashSet<int>(nums);

            if(set.Count<nums.Length)
            {
                Console.WriteLine("Dup");
            }
        }
    }