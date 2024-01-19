func findMaxConsecutiveOnes(nums []int) int {
    maxValue := 0
    count := 0

    for _, n := range nums {
        if n == 1 {
            count++
            maxValue = max(maxValue, count)
        } else {
            count = 0
        }
    }

    return maxValue
}

func max(a,b int) int {
    if a < b {
        return b
    }
    return a
}