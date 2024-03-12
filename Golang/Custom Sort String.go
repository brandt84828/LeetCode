func customSortString(order string, s string) string {
    count := count(s)
    var in_order string
    for i:=0; i<=len(order)-1; i++ {
        freq, exists := count[order[i]]
        if exists {
            for j:=0; j<freq; j++ {
                in_order += string(order[i])
            }
            s = strings.Replace(s, string(order[i]), "", -1)
        }
    }
    return in_order + s
}


func count(s string) map[byte]int {
    count := make(map[byte]int)
    for i:=0; i<=len(s)-1; i++ {
        _, exists := count[s[i]]
        if exists {
            count[s[i]]++
        } else {
            count[s[i]] = 1
        }
    }
    return count
}