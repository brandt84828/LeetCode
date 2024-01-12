class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        count = 0
        for char in columnTitle[::-1]:
            total = total + pow(26, count) * (ord(char) - 64)
            count = count + 1
        
        return total