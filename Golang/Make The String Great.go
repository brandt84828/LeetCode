//#1
func makeGood(s string) string {
    bytes := make([]byte, 0) //byte slice
    for i, _ := range s {
        n := len(bytes)
        if n > 0 && (bytes[n-1] == s[i] - 'a' + 'A' || bytes[n-1] == s[i] - 'A' + 'a') {
            bytes = bytes[:n-1]
        } else {
            bytes = append(bytes, s[i])
        }
    }
    return string(bytes)
}

//#2
func makeGood(s string) string {
	if len(s) < 2 {
		return s
	}

	stack := make([]rune, 0, len(s))
	for _, r := range s {
		if len(stack) == 0 {
			stack = append(stack, r)
			continue
		}

		top := stack[len(stack)-1]
		if AreBadAdjacents(top, r) {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, r)
		}
	}

	return string(stack)
}

func AreBadAdjacents(a, b rune) bool {
	return mod(a-b) == 32
}

func mod(x int32) int32 {
	if x < 0 {
		return -x
	}
	return x
}