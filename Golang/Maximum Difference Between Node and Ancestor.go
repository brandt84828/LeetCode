/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxAncestorDiff(root *TreeNode) int {
    if root == nil {
        return 0
    }
    return dfs(root, root.Val, root.Val)
}

func dfs(node *TreeNode, high int, low int) int {
    if node == nil{
        return high - low
    }
    high =  max(high, node.Val)
    low = min(low, node.Val)
    return max(dfs(node.Left, high, low), dfs(node.Right, high, low))
}

func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}