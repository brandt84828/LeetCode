#1
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in nums:
            psum += i
            res += c[psum - goal]
            c[psum] += 1
        return res

        # Time O(n) Space O(n)

#2
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0: return 0
            res = i = 0
            for j in range(len(nums)):
                goal -= nums[j]
                while goal < 0:
                    goal += nums[i]
                    i += 1
                res += j - i + 1
            return res
        return atMost(goal) - atMost(goal - 1)

        # Time O(n) Space O(1)