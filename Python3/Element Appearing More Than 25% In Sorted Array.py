#1
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + n]:
                return arr[i]

#2
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def findIndexOfFirst(x):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        for q in range(1, 4):
            idx = int(q * len(arr) / 4)
            start = findIndexOfFirst(arr[idx])
            if arr[start] == arr[start + len(arr)//4]:  #  check the length is at least 25%
                return arr[start]