// 1
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    if root == nil {
        return 0
    }
    if root.Left != nil && root.Left.Left == nil && root.Left.Right == nil {
        return root.Left.Val + sumOfLeftLeaves(root.Right)
    }
    return sumOfLeftLeaves(root.Left) + sumOfLeftLeaves(root.Right)
}

// 2
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    res := 0
    var dfs func(*TreeNode, bool)
    dfs = func(node *TreeNode, flag bool) {
        if node == nil {
            return
        }
        if node.Left == nil && node.Right == nil && flag {
            res += node.Val
        }
        dfs(node.Left, true)
        dfs(node.Right, false)
    }
    dfs(root, false)
    return res
}