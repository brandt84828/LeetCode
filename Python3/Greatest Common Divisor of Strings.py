#1
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]

#Assuming that str1 and str2 share a common divisor string 't', we can represent str1 as t + t + t + ... (m times) = t * m, and str2 as t + t + t + ... (n times) = t * n. 
#By combining these two strings, we obtain str1 + str2 = t * (m+n), which is equivalent to str2 + str1. 
#Therefore, if str1 + str2 == str2 + str1, we can derive a solution from it.

#2 regex
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            return b if a == 0 else gcd(b % a, a)
        d = gcd(len(str1), len(str2))
        gcd_str = str1[0 : d]
        ptn = '(' + gcd_str + ')+'
        return gcd_str if re.fullmatch(ptn, str1) and re.fullmatch(ptn, str2) else ''