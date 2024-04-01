#1
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        res = -1

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res = nums1[i]
                return res
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return res

#2
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2), default=-1)
        # default => if min value = empty then return default