#1
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = root.val
        while root:
            if abs(res - target) >= abs(root.val - target):
                res = root.val
           
            if target < root.val:
                root = root.left
            else:
                root = root.right
       
        return res

