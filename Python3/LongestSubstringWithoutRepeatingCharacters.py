class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        length = 0
        count = {}
        for r in range(len(s)):

            if s[r] in count:
		# 取得重複值的下一位，使用max避免l跑回去比原本還前面的index
                l = max(count[s[r]]+1, l)
                
            count[s[r]] = r
            length = max(length,r - l + 1)

        return length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        length = 0
        hashset = {}
        for r in range(len(s)):

            if s[r] in hashset:
                l = max(hashset[s[r]]+1, l)
                
            hashset[s[r]] = r
            length = max(length,r - l + 1)
           # hashset[s[r]] = hashset[s[r]] + 1

        return length