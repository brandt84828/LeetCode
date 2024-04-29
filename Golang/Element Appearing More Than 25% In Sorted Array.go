func findSpecialInteger(arr []int) int {
    n := len(arr)
    target := n / 4
    for _, i := range []int{n / 4, n / 2, 3 * n / 4} {
        v := arr[i]
        l, r := 0, i
        for l < r {
            m := (l + r) / 2
            if arr[m] == v {
                r = m
            } else {
                l = m + 1
            }
        }
        if arr[r + target] == v {
            return v
        }
    }
    return 0
}