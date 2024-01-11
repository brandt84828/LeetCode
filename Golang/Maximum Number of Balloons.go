//#1
func maxNumberOfBalloons(text string) int {
    m := map[rune]int{'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n':0}
    for _, char := range text {
        if _, ok := m[char]; ok {
            m[char] = m[char] + 1
        } 
    }

    count := min(m['b'], min(m['a'], m['n']))
    count = min(count, min(m['l'] / 2, m['o'] / 2))

    return count
}

func min(a,b int) int {
    if a < b {
        return a
    }
    return b
}

//#2
func maxNumberOfBalloons(text string) int {
    b,a,l,o,n := 0,0,0,0,0
    for _, r := range text{
        switch r {
            case 'b':
                b++
            case 'a':
                a++
            case 'l':
                l++
            case 'o':
                o++
            case 'n':
                n++
        }
    }
    
    res := min(b, min(a,n))
    res = min(res, min(l/2,o/2))
    return res
}

func min(a,b int) int{
    if a < b {
        return a
    }
    return b
}