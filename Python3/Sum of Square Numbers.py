func judgeSquareSum(c int) bool {
    left, right := 0, int(math.Sqrt(float64(c)))
    for left <= right {
        cur := left * left + right * right
        if cur == c {
            return true
        } else if cur < c {
            left++
        } else {
            right--
        }
    }
    return false
}