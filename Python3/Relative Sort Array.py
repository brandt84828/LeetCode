#1
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = {}
        for i in range(len(arr2)):
            m[arr2[i]] = i

        return sorted(arr1, key=lambda x: m.get(x , 1000 + x)) #1000 avoid non-exist value < exist value

#2
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=(arr2 + sorted(arr1)).index)