func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))
    res[0] = 1
    for i:=1;i < len(nums);i++ {
        res[i] = res[i-1] * nums[i-1]
    }
    temp := 1
    for i:=len(nums)-1;i > -1;i-- {
        res[i] = res[i] * temp
        temp = temp * nums[i]
    }
    return res
}