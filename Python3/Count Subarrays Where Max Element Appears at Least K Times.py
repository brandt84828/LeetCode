class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ma = max(nums)
        res = cur = i = 0
        for j in range(len(nums)):
            cur += nums[j] == ma # cur + 1 when nums[j] == ma
            while cur >= k:
                cur -= nums[i] == ma
                print(cur)
                i += 1
            res += i
        return res

#Let array= [1, 2, 4, 4, 2, 3] and k=2
#If there are 2 elements on the left side, I can create 3 different types of arrays: 
#[1, 2, 4, 4], [2, 4, 4], and [4, 4].

#if i move right by one it will create 3 new arrays
#[1, 2, 4, 4, 1],  [2, 4, 4, 1], and [4, 4, 1]

#[1, 2, 4, 4, 1, 3],  [2, 4, 4, 1, 3], and [4, 4, 1, 3]
#as i move right by one 3 new arrays are creating
#that's why every time i am incrementing ans by l