func findMin(nums []int) int {
    start := 0
    end := len(nums) - 1
    min := 5000

    for start < end {
        mid := start + (end - start) / 2
        min = getMin(min, nums[mid])
        if nums[mid] > nums[end] {
            start = mid + 1
        } else {
            end = mid - 1
        }
    }
    return getMin(min, nums[start])
}

func getMin(a int, b int) int {
    if a < b {
        return a
    }
    return b
}

//# 2
func findMin(nums []int) int {
    res := nums[0]
    l, r := 0, len(nums)-1
    
    for l <= r {
        p := (l+r) / 2
        if nums[p] >= nums[0] {
            l = p+1
        } else {
            if nums[p] < res {
                res = nums[p]
            }
            r = p-1
        }
    }
    
    return res
}
