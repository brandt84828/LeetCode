class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack


#2

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for c in s:
            if c in Map:
                stack.append(c)
            elif len(stack) > 0 and Map[stack[-1]] == c :
                stack.pop()
            else:
                return False

        return len(stack)==0

#3

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "]":"[", "}":"{"}
        stack=[]

        for c in s:
            if c in mapping and len(stack) > 0:
                v = stack.pop()
                if mapping[c] != v:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
