# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None:
                return 0
            l = check(root.left)
            r = check(root.right)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return max(l,r) + 1
        return check(root) != -1


#2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, max(left[1], right[1])+1]
        return dfs(root)[0]