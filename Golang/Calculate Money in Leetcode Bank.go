func totalMoney(n int) int {
    week := 0
    total := 0
    for i:=1;i<=n;i++ {
        total = total + (i - 7 * week) + week
        if i % 7 == 0 {
            week++
        }
    }
    return total
}