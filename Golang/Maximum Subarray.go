func maxSubArray(nums []int) int {
    res := nums[0]
    total := 0
    for _, n := range nums {
        total = total + n
        res = max(res, total)
        if total < 0 {
            total = 0
        }
    }
    return res
}

func max(a int, b int) int {
    if a < b {
        return b
    }
    return a
}