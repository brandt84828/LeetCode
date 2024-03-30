#1
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        ans = ii = 0
        for i, x in enumerate(nums): 
            freq[x] += 1
            while freq[x] > k: 
                freq[nums[ii]] -= 1
                ii += 1
            ans = max(ans, i-ii+1)
        return ans 

#2
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()
        res = i = 0
        for j in range(len(nums)):
            count[nums[j]] += 1
            while count[nums[j]] > k:
                count[nums[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res