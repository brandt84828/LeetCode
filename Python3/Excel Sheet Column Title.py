#1
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J",11:"K",12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}
        res = ""

        while columnNumber > 0:
            columnNumber = columnNumber - 1
            cur = columnNumber % 26
            columnNumber = columnNumber // 26
            res += d[cur+1]

        return res[::-1]class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J",11:"K",12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}
        res = ""

        while columnNumber > 0:
            columnNumber = columnNumber - 1
            cur = columnNumber % 26
            columnNumber = columnNumber // 26
            res += d[cur+1]

        return res[::-1]

#2
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            cur = columnNumber % 26
            columnNumber = columnNumber // 26
            res += chr(cur + ord('A'))

        return res[::-1]

#3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=""
        while columnNumber:
            columnNumber=columnNumber-1
            ans=abc[columnNumber%26]+ans
            columnNumber=columnNumber//26
        return ans