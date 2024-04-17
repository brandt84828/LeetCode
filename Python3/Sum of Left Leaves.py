#1 DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)   # isn't leave



#Another
#def sumOfLeftLeaves(self, root, isLeft=False):
#    if not root: return 0
#    if not (root.left or root.right): return root.val * isLeft
#    return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)

#2 BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        sum = 0
        while queue:
            k = len(queue)
            for i in range(k):
                cur = queue.popleft()
                if cur.left:
                    if not cur.left.left and not cur.left.right:
                        sum = sum + cur.left.val
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return sum