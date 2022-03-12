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
public class Solution100 {
    public bool IsSameTree(TreeNode p, TreeNode q) {
        
        if(p==null || q==null) return p==q;
        
        if(p.val==q.val)
        {
            return IsSameTree(p.left,q.left) && IsSameTree(p.right,q.right);
        }
        else
        {
            return false;
        }
    }
}