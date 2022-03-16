public class Solution946 {
    public bool ValidateStackSequences(int[] pushed, int[] popped) {
        
        int pushLen = pushed.Length;
        int j = 0;
        Stack<Int32> stack = new Stack<Int32>();
        
        foreach(int x in pushed)
        {
            stack.Push(x);
            
            while( stack.Count!=0 && j<pushLen && stack.Peek()==popped[j])
            {
                stack.Pop();
                j++;
            }
        }
        
        return j==pushLen;
        
    }
}