func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
    treeOne := getLeaves(root1, []int{})
    treeTwo := getLeaves(root2, []int{})

    if len(treeOne) != len(treeTwo) {
        return false
    }

    for i := range treeOne {
        if treeOne[i] != treeTwo[i] {
            return false
        }
    }
    return true
}

func getLeaves(root *TreeNode, curLeaves []int) []int {
    if root == nil {
        return []int{}
    }

    if root.Left == nil && root.Right == nil {
        return append(curLeaves, root.Val)
    }

    l := append(curLeaves, getLeaves(root.Left, curLeaves)...)
    return append(l, getLeaves(root.Right, curLeaves)...)
}