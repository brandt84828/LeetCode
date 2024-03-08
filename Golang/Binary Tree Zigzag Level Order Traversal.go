/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	ans := [][]int{}
    // handle base case
	if root == nil {
		return ans
	}

	even := true

	queue := []*TreeNode{root}

	for len(queue) > 0 {

		l := len(queue)

        // Create a subList to add to answer for each row
		subList := []int{}

		for i := 0; i < l; i++ {
			node := queue[i]

            // Process left 
			if node.Left != nil {
				queue = append(queue, node.Left)
			}

            // Process Right 
			if node.Right != nil {
				queue = append(queue, node.Right)
			}

            // even, add the node value at the end of sublist
			if even {
				subList = append(subList, node.Val)
			} else {
                // odd, add the node value as the first value of sublsit
				subList = append([]int{node.Val}, subList...)
			}
		}
		queue = queue[l:]
        // change even to odd
		even = !even
        // Add the sublist to final ans
		ans = append(ans, subList)
	}
	return ans
}