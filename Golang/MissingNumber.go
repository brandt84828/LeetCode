func missingNumber(nums []int) int {

    ans := len(nums)

    for index, value := range nums {
        ans = ans ^ index ^ value
    }

    return ans
    
}