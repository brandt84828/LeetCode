func bulbSwitch(n int) int {
    res := 0
    for i:=1;i*i<=n;i++{
        res++
    }
    return res
}