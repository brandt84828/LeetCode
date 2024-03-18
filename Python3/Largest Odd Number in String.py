#1
class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ""
        for i in range(len(num)-1,-1,-1):
            if res == "":
                if int(num[i]) % 2 == 1:
                    res = res + num[i]
            else:
                res = num[i] + res
        
        return res

#2 Bit Operation
class Solution:
      def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):  # traverse from right to left
            if int(num[i])&1:  # if number is odd
                return num[:i+1]
        return ''

#3
class Solution:
      def largestOddNumber(self, num: str) -> str:
            for i in range(len(num) - 1, -1, -1) :
                if num[i] in {'1','3','5','7','9'} :
                    return num[:i+1]
            return ''