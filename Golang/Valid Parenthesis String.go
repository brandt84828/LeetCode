func checkValidString(s string) bool {
    ma := 0
    mi := 0

    for _, b := range s {
        if b == '(' {
            ma++
            mi++
        }
        if b == ')' {
            ma--
            mi = max(mi-1, 0)
        }
        if b ==  '*' {
            ma++
            mi = max(mi-1, 0)
        }
        if ma < 0 {
            return false
        }
    }
    return mi == 0

}

func max(a int, b int) int {
    if a < b {
        return b
    }
    return a
}