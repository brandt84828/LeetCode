class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs or len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            compare = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or compare != strs[j][i]:
                    return strs[0][0:i]

        return strs[0]
