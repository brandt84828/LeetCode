func maxDepth(s string) int {
    res := 0
    count := 0
    for _, v := range s {
        if string(v) ==  "(" {
            count++
            if count > res {
                res = count
            }
        }
        if string(v) == ")" {
            count--
        }
    }
    return res
}
