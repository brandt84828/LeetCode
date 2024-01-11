#1
class Solution:
    def makeGood(self, s: str) -> str:
        result = [] #stack
        for c in s:
            if not result:
                result.append(c)
            elif result[-1].isupper() and result[-1].lower() == c: #???? ??????
                result.pop()
            elif result[-1].islower() and result[-1].upper() == c: #???? ??????
                result.pop()
            else:
                result.append(c)
        return ''.join(result)

#2
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []        
        for c in s:
            if stack and stack[-1] == c.swapcase():
                stack.pop()
            else:
                stack.append(c)
                
        return "".join(stack)