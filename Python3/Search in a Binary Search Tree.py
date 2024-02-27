#1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

#2 Better
class Solution:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root