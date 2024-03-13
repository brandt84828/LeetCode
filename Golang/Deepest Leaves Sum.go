/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deepestLeavesSum(root *TreeNode) int {
    res := 0
    q := []*TreeNode{root}

    for len(q) > 0 {
       sum := 0
       l := len(q)

        for i:=0;i<l;i++ {
            node := q[0]
            //pop
            q = q[1:]
            sum += node.Val

            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        res = sum
    }
    return res
}