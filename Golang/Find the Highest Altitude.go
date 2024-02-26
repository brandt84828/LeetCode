func largestAltitude(gain []int) int {
    total := 0
    res := 0
    for _, v := range gain {
        total += v
        if total > res {
            res = total
        }
    }
    return res
}