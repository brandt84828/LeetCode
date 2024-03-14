func pivotInteger(n int) int {
    total := (1 + n) * n / 2
    for i:=1; i <= n; i++ {
        pivot := (1 + i) *  i / 2
        if total - pivot + i == pivot {
            return i
        }
    }
    return -1
}