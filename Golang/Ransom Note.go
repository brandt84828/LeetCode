func canConstruct(ransomNote string, magazine string) bool {
    if len(ransomNote) > len(magazine) {
        return false
    }
    
    table := make(map[rune]int, 26)
    for _, v := range magazine {
        table[v] = table[v] + 1
    }
    for _, v := range ransomNote {
        table[v] = table[v] - 1
        if table[v] < 0 {
            return false
        }
    }

    return true

}