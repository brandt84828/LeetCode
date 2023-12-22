func missingNumber(nums []int) int {

    ans := len(nums)

    for index, value := range nums {
        ans = ans ^ index ^ value
    }

    return ans
    
}

#2

func missingNumber(nums []int) int {
    res := len(nums)
    
    for i := 0; i < len(nums); i++ {
        res += i - nums[i]
    }
    return res
}