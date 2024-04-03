//1
func vowelStrings(words []string, left int, right int) int {
    res := 0
    for i:=left;i<=right;i++ {
        if check(string(words[i][0])) && check(string(words[i][len(words[i])-1])) {
            res++
        }
    }
    return res
}

func check(word string) bool {
    if word == "a" || word == "e" || word == "i" || word == "o" || word == "u" {
        return true
    }
    return false
}

//2
func vowelStrings(words []string, left int, right int) int {
	res := 0
	for _, v := range words[left : right+1] {
		if IsVowels(v[0]) && IsVowels(v[len(v)-1]) {
			res++
		}
	}
	return res
}

func IsVowels(s uint8) bool {
	switch s {
	case 'u', 'o', 'a', 'i', 'e':
		return true
	}
	return false
}

//3
var vowels = map[byte]struct{}{
    'a': struct{}{},
    'e': struct{}{}, 
    'i': struct{}{},
    'o': struct{}{},
    'u': struct{}{},
}

func vowelStrings(words []string, left int, right int) int {
    words = words[left:right+1]

    count := 0
    for _, w := range words {
        first := w[0]
        if _, ok := vowels[first]; !ok {
            continue
        }
        last := w[len(w)-1]
        if _, ok := vowels[last]; !ok {
            continue
        }
        count++
    }
    return count
}