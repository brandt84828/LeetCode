/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func distributeCoins(root *TreeNode) int {
  res := 0
  coinsOf(root, &res)
  return res
}

func coinsOf(node *TreeNode, res *int) int {
  if node == nil {
    return 0
  }

  lcoins := coinsOf(node.Left, res)
  rcoins := coinsOf(node.Right, res)

  // cost of moving coins in subtrees to current node
  (*res) += abs(lcoins)+abs(rcoins)

  coins := node.Val-1
  coins += lcoins+rcoins

  return coins
}

func abs(num int) int {
  if num < 0 {
    return -num
  }
  return num
}