func maxSubarrayLength(nums []int, k int) int {
    m := make(map[int]int, len(nums))
    start := 0
    res := 0
    
    for i, v := range nums {
        m[v] += 1
        for m[v] > k {
            m[nums[start]] -= 1
            start++
        }
        res = max(res, i - start + 1)
    }
    return res
}

func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}