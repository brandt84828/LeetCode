/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
    if root != nil && val < root.Val {
        return searchBST(root.Left, val)
    } else if root != nil && val > root.Val {
        return searchBST(root.Right, val)
    } else {
        return root
    }
}