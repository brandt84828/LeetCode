/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution111 {
    public int MinDepth(TreeNode root) {
        
        /// DFS
        if (root == null)	return 0;
        if (root.left == null)	return MinDepth(root.right) + 1;
        if (root.right == null) return MinDepth(root.left) + 1;
        return Math.Min(MinDepth(root.left),MinDepth(root.right)) + 1;
        
    }
}


public class Solution111 {
    public int MinDepth(TreeNode root) {
        
        ///BFS
        if (root == null) return 0;
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        int depth = 0;
        while (queue.Count != 0)
        {
            int size = queue.Count;
            depth++;
            for (int i = 0; i < size; ++i)
            {
                var curr = queue.Dequeue();
                
                if (curr.left == null && curr.right == null)
                {
                    return depth;
                }
                
                if (curr.left != null) queue.Enqueue(curr.left);
                
                if (curr.right != null) queue.Enqueue(curr.right);
            }
        }
        return depth;
        
    }
}