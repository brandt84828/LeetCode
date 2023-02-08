func climbStairs(n int) int {
    n1 := 2
    n2 := 3
    if n <= 3 {
        return n
    }

    for i:=4;i < n + 1;i++ {
        temp := n1 + n2
        n1 = n2
        n2 = temp
    }
    return n2
}