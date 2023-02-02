func strStr(haystack string, needle string) int {
    m := len(needle)
    n := len(haystack)

    for start:=0;start < n - m + 1;start++ {
        for i:=0;i < m;i++ {
            if needle[i] != haystack[start+i] {
                break
            }
            if i == m - 1 {
                return start
            }
        }
    }
    return -1
}