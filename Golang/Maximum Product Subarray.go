func maxProduct(nums []int) int {
    r := nums[0]
    max:=r
    min:=r
    for i:=1;i < len(nums);i++ {
        if nums[i] < 0 {
            max, min = min, max
        }

        max = maxFunc(nums[i], max*nums[i])
        min = minFunc(nums[i], min*nums[i])

        r = maxFunc(r, max)
    }
    return r
}

func maxFunc(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func minFunc(a, b int) int {
    if a > b {
        return b
    }
    return a
}