func rob(nums []int) int {
    //[rob1, rob2, n, n+1, ...]
    rob1, rob2 := 0, 0
    for _, n :=range nums {
        temp := max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    }
    return rob2
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}