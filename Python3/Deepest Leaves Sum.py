# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# lee215
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)

#BFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q, ans, qlen, curr = [root], 0, 0, 0
        while len(q):
            qlen, ans = len(q), 0
            for _ in range(qlen):
                curr = q.pop(0)
                ans += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        return ans

#DFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        def dfs(node: TreeNode, lvl: int):
            if lvl == len(sums): sums.append(node.val)
            else: sums[lvl] += node.val
            if node.left: dfs(node.left, lvl+1)
            if node.right: dfs(node.right, lvl+1)
        dfs(root, 0)
        return sums[-1]