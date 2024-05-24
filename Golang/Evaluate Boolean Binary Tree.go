/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func evaluateTree(root *TreeNode) bool {
    return helper(root)
}

func helper(root *TreeNode) bool {
    if root.Val == 0 || root.Val == 1 {
        return root.Val == 1
    } else if root.Val == 2 {
        return helper(root.Left) || helper(root.Right)
    } else if root.Val == 3 {
        return helper(root.Left) && helper(root.Right)
    }

    return false
}