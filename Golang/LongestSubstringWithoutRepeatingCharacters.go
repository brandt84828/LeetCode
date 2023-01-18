func lengthOfLongestSubstring(s string) int {

    l := 0
    length := 0
    count := make(map[byte]int, len(s))

    for r := 0; r < len(s); r++ {

        if _, ok := count[s[r]]; ok {
            l = max(count[s[r]] + 1, l)
        }

        count[s[r]] = r
        length = max(length, r - l + 1)
    }

    return length
    
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}