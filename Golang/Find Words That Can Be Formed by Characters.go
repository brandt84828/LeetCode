func countCharacters(words []string, chars string) int {
    charSet := make([]int, 26)
    
    for i := 0; i < len(chars); i++ {
        charSet[int(chars[i] - 'a')]++
    }
    
    sum := 0
    
    for _, word := range words {
        currentCharSet := make([]int, 26)
        copy(currentCharSet, charSet)
        
        isValid := true
        
        for i := 0; i < len(word); i++ {
            currentCharSet[int(word[i] - 'a')]--
            
            if currentCharSet[int(word[i] - 'a')] < 0 {
                isValid = false
                break
            }
        }
        
        if isValid {
            sum += len(word)
        }
    }
    
    return sum
}