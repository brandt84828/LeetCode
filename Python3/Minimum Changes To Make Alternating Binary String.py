#1
class Solution:
    def minOperations(self, s: str) -> int:
        length = len(s)
        ans1 = ["0"] * length
        ans2 = ["0"] * length

        for i in range(len(s)):
            if i % 2 == 0:
                ans1[i] = "1"
            else:
                ans2[i] = "1"

        str1 = ''.join(ans1)
        str2 = ''.join(ans2)

        diff1, diff2 = 0, 0

        for i in range(len(s)):
            if s[i] != str1[i]:
                diff1+=1
            if s[i] != str2[i]:
                diff2+=1

        return min(diff1, diff2)
        
#2
class Solution:
    def minOperations(self, s: str) -> int:
        res = sum(i % 2 == int(c) for i, c in enumerate(s))
        return min(res, len(s) - res)
        

# lee215

#Small observation that the sequence of index is [0,1,2,3..],
#if we get its module by 2, we get [0,1,0,1,0..],
#which is the alternating binary sequence we want.

#So we iterate the string,
#check if the characters[i] is same as the i % 2.
#Note that s[i] is a character,
#and s[i] - '0' making it to integer.

#We accumulate the number of difference,
#which is the number of operation to make it into 01 string.

#We can do the same to find out res,
#the number of operation for 10 string.
#But we don't have to,
#becaue this equals to s.length - res.