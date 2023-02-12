func canJump(nums []int) bool {
    target := len(nums) - 1
    for i:=len(nums)-2;i>-1;i-- {
        if nums[i] + i >= target {
            target = i
        }
    }
    return target == 0
}