func pivotIndex(nums []int) int {
    left, right := 0, sum(nums)
    for i, v := range nums {
        right -= v
        if left == right {
            return i
        }
        left += v
    }    
    return -1
}

func sum(nums []int) int {
    total := 0
    for _, v := range nums {
        total += v
    }
    return total
}