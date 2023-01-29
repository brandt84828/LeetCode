class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfsHelper(digits, index, letters, sb, res):
            if index == len(digits):
                res.append(sb)
                return
            values = letters[int(digits[index])]
            for c in values:
                sb = sb + c
                dfsHelper(digits, index + 1, letters, sb, res)
                sb = sb[0:-1]

        res = []
        sb = ""
        index = 0
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        if not digits or len(digits) == 0:
            return res
        dfsHelper(digits, index, letters, sb, res)

        return res
