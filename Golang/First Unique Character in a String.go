//1
func firstUniqChar(s string) int {
	d := map[byte]int{}

	for i := 0; i < len(s); i++ {
		d[s[i]]++
	}

	for i := 0; i < len(s); i++ {
		if d[s[i]] == 1 {
			return i
		}
	}

	return -1
}

//2
func firstUniqChar(s string) int {
	symbols := [26]int16{}

    for i := range s {
        symbols[s[i]-'a']++
    }
    for i := range s {
        if symbols[s[i]-'a'] == 1 {
            return i
        }
    }
    return -1
}