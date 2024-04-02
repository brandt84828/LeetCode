func maxProductDifference(nums []int) int {
    min1, min2 := math.MaxInt, math.MaxInt
    max1, max2 := math.MinInt, math.MinInt

    for _, n := range nums {
        if n <= min1 {
            min1, min2 = n, min1
        } else if n < min2 {
            min2 = n
        }
        if n >= max1 {
            max1, max2 = n, max1
        } else if n > max2 {
            max2 = n
        }
    }
    return max1*max2-min1*min2
}