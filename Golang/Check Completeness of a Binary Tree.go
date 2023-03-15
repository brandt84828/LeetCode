/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isCompleteTree(root *TreeNode) bool {
    if root == nil {
        return true
    }

    q := []*TreeNode{root}
    flag := false
    for len(q) > 0 {
        node := q[0]
        q = q[1:]
        if node == nil {
            flag = true
        } else {
            if flag {
                return false
            }
            q = append(q, node.Left, node.Right)
        }
    }
    return true
    
}