func scoreOfString(s string) int {
    res := 0
    for i:=0;i<len(s)-1;i++ {
        temp := abs(int(s[i]) - int(s[i+1]))
        res += temp
    }
    return res
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}