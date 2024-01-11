func minStartValue(nums []int) int {
    currSum := 0
    minSum := 0
    for _, num := range nums {
        currSum = currSum + num
        minSum = min(minSum, currSum)
    }
    if minSum > 0 {
        return 1
    } else {
        return 1 - minSum
    }
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}