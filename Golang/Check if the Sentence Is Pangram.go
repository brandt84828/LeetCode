//#1
func checkIfPangram(sentence string) bool {
    c := make(map[rune]int)
    for _, s := range sentence {
        if _, ok := c[s]; ok {
            
        } else {
            c[s] = 1
        }
    }
    return len(c) == 26
}