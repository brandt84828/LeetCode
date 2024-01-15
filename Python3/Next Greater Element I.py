#1
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None

        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:       # if stack is not empty, then compare it's last element with nums2[i]
                mapping[stack[-1]] = nums2[i]           # if the new element is greater than stack's top element, then add this to dictionary 
                stack.pop()                             # since we found a pair for the top element, remove it.
            stack.append(nums2[i])                      # add the element nums2[i] to the stack because we need to find a number greater than this

        for element in stack:                           # if there are elements in the stack for which we didn't find a greater number, map them to -1
            mapping[element] = -1

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result

#2
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        st = []
        ans = []
        
        for x in nums2:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(d.get(x, -1))
            
        return ans