func sumOfSquares(nums []int) int {
    res := 0
    n := len(nums)
    for i, v := range nums {
        if n % (i+1) == 0 {
            res += v * v
        }
    }
    return res
}