func makeEqual(words []string) bool {
    charCount := [26]int{}
    n := len(words)
    for _, word := range words {
        for _, c := range word {
            charCount[c - 'a']++
        }
    }
    for _, c := range charCount {
        if c % n != 0 {
            return false
        }
    }
    return true
}