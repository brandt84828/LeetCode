class Solution(object):
   def largestUniqueNumber(self, A):
      d = {}
      ans = -1
      for i in A:
         if i not in d:
            d[i]=1
         else:
            d[i] +=1
      for a,b in d.items():
         if b == 1:
            ans = max(a,ans)
      return ans