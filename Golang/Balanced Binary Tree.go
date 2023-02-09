/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    return check(root) != -1
}

func check(root *TreeNode) int {
    if root == nil {
        return 0
    }
    left := check(root.Left)
    right := check(root.Right)
    if left == -1 || right == -1 || abs(left - right) > 1 {
        return -1
    }
    return max(left, right) + 1
}
func abs (a int) int {
    if a < 0 {
        return a * -1
    }
    return a
}
func max(a int, b int) int {
    if a < b {
        return b
    }
    return a
}