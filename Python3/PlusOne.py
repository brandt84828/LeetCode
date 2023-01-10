class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            digits[i]=digits[i]+1
            if digits[i]==10:
                digits[i]=0
                if digits[0]==0:
                    digits.insert(0,1)
                continue
            else:
                break
        
        return digits

#2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        one = 1
        i = 0
        digits = digits[::-1]

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    one = 0
                    digits[i] = digits[i] + 1
            else:
                digits.append(1)
                one = 0
            i = i + 1

        return digits[::-1]
            
