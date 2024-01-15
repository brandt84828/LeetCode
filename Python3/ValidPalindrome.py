# 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.check(s[l]):
                l += 1
            while l < r and not self.check(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def check(self, c):
        return (
            # ord-->convert to decimal system	
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

# 2 keep char and digital => use[::-1] to check palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for value in s:
            if value.isalpha() == True or value.isnumeric() == True:
                new = new + value

        if new.lower() == new[::-1].lower():
            return True
        else:
            return False