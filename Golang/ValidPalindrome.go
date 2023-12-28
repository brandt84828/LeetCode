//import "strings"

func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	l, r := 0, len(s)-1
	for l < r {
		for l < r && !isChar(s[l]) {
			l++
		}
		for l < r && !isChar(s[r]) {
			r--
		}
		if s[l] != s[r] {
			return false
		}
		l++
		r--
	}
	return true
}

// 判斷 c 是否為字或數
func isChar(c byte) bool {
	if ('a' <= c && c <= 'z') || ('0' <= c && c <= '9') {
		return true
	}
	return false
}
    

#2
func isPalindrome(s string) bool {
    f := func(r rune) rune {
        if !unicode.IsLetter(r) && !unicode.IsNumber(r) {
            return -1
        }
        
        return unicode.ToLower(r)
    }
    s = strings.Map(f, s)
    
    i, j := 0, len(s)-1
    
    for i < j {
        if s[i] != s[j] {
            return false
        }
        
        i = i+1
        j = j-1
    }
    
    return true
}
