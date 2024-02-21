#1
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = {}
        n2 = {}
        res1 = []
        res2 = []

        for n in nums1:
            n1[n] = 1
        for n in nums2:
            n2[n] = 1
        
        for n in nums1:
            if n not in n2 and n not in res1:
                res1.append(n)
        for n in nums2:
            if n not in n1 and n not in res2:
                res2.append(n)

        return [res1, res2]


#2
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [set1 - set2, set2 - set1]
