//1
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findBottomLeftValue(root *TreeNode) int {
    s := []*TreeNode{root}
    var res int
    for s != nil {
        res = s[0].Val
        s = do(s)
    }
    return res
    
}


func do(s []*TreeNode) []*TreeNode {
    var res []*TreeNode
    for _, v := range s {
        if v.Left != nil {
            res = append(res, v.Left)
        }
        if v.Right != nil {
            res = append(res, v.Right)
        }
    }
    return res
}

//2
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findBottomLeftValue(root *TreeNode) int {
    que := []*TreeNode{root}

    var popped *TreeNode

    for len(que) > 0 {
    popped = que[len(que) - 1]
    que = que[:len(que) - 1]

    if popped.Right != nil {
        que = append([]*TreeNode{popped.Right}, que...)
    }

    if popped.Left != nil {
        que = append([]*TreeNode{popped.Left}, que...)
    }
    }

    return popped.Val
}