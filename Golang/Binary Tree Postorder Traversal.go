/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type Res struct {
	Res []int
}

func postorderTraversal(root *TreeNode) []int {
	r := Res{}
	r.traversal(root)
	return r.Res
}

func (r *Res) traversal(node *TreeNode) {
	if node != nil {
		r.traversal(node.Left)
		r.traversal(node.Right)
		r.Res = append(r.Res, node.Val)
    }
}