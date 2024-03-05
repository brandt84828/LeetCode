func getAverages(nums []int, k int) []int {
    res := make([]int, len(nums))
    diameter := 2*k+1
    left := 0
    curWindowSum := 0
    for i:=0;i<len(nums);i++{
        res[i] = -1
    }
    for right:=0;right<len(nums);right++ {
        curWindowSum += nums[right]
        if right-left+1 >= diameter {
            res[left+k] = curWindowSum / diameter
            curWindowSum -= nums[left]
            left = left + 1
        }
    }
    return res
}