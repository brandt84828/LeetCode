func equalSubstring(s string, t string, maxCost int) int {
    var curCost, ans, l int
    for r := 0; r < len(s); r++ {
        curCost += abs(int(s[r]) - int(t[r]))
        for curCost > maxCost {
            curCost -= abs(int(s[l]) - int(t[l]))
            l++
        }
        ans = max(ans, r - l + 1)
    }
    return ans
}

func abs(n int) int {
    if n > 0 { return n }
    return -n
}