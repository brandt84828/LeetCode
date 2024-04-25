//1
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rangeSumBST(root *TreeNode, low int, high int) int {
    sum := 0
	var recur func(root *TreeNode)

	recur = func(root *TreeNode) {
		if root.Val >= low && root.Val <= high {
			sum += root.Val
		}
		if root.Left != nil {
			recur(root.Left)
		}
		if root.Right != nil {
			recur(root.Right)
		}
	}
	recur(root)

	return sum
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
func rangeSumBST(root *TreeNode, low int, high int) int {
    if root == nil { return 0 }

    if root.Val < low {
        return rangeSumBST(root.Right, low, high)
    } else if root.Val > high {
        return rangeSumBST(root.Left, low, high)
    } else {
        return root.Val+ rangeSumBST(root.Left, low, high) + rangeSumBST(root.Right, low, high)
    }
}