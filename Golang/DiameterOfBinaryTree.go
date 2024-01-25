//1
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
    res := 0
    maxDepth(&res, root)
    return res
}

func maxDepth(res *int, root *TreeNode) int {
    if root == nil {
        return 0
    }

    left := maxDepth(res, root.Left)
    right := maxDepth(res, root.Right)
    *res = max(*res, left + right)
    return max(left, right) + 1
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
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
 var maxD int

 func diameterOfBinaryTree(root *TreeNode) int {
     maxD = 0
     find(root)
     return maxD
 }
 
 func find(root *TreeNode) int {
     if root == nil {
         return 0
     }
     left := find(root.Left)
     right := find(root.Right)
     localMax := left + right
     maxD = max(maxD, localMax)
     return max(left, right) + 1
 }
 
 func max(a, b int) int {
     if a > b {
         return a
     }
     return b
 }