#1
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        N=len(nums)
        
        # for each index we have to check if all element before it is smaller than this
        min_=[None for _ in range(N)]
        mi_=float('-inf')
        for i in range(N):
            min_[i]=mi_
            mi_=max(nums[i],mi_)
        print(min_)
        # for each index we have to check if all element after it is bigger than this       
        max_=[None for _ in range(N)]
        mx_=float('inf')
        for i in range(N-1,-1,-1):
            max_[i]=mx_
            mx_=min(mx_,nums[i])
        print(max_)
        ans=0
        for i in range(1,N-1):
            if min_[i]<nums[i]<max_[i]:
                ans+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                ans+=1
        return ans

#2
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        left, right = [], []
        largest = nums[0]
        smallest = nums[-1]
        for n in nums:
            left.append(largest)
            if n > largest:
                largest = n
        for n in nums[::-1]:
            right.append(smallest)
            if n < smallest:
                smallest = n
        right = right[::-1]
        ans = 0
        for i in range(1, len(nums)-1):
            # print(i, nums[i], left, right)
            if nums[i] > left[i] and nums[i] < right[i]: ans += 2
            elif nums[i] > nums[i-1] and nums[i] < nums[i+1]: ans +=1
        return ans