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
public class Solution700 {
    public TreeNode SearchBST(TreeNode root, int val) {
        
        if(root==null) return root;
        if(root.val==val)
        {
            return root;
        }
        else
        {
            return val < root.val ? SearchBST(root.left,val):SearchBST(root.right,val);
        }

        /*
        iteration

        while(root != null && root.val != val){
            root = val<root.val? root.left:root.right;
        }
        return root;

        */
        
    }
}