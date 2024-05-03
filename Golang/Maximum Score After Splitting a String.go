func maxScore(s string) int {
    var result, totalOnes, leftZeros, leftOnes int
    
    for _, char := range s {
        if char == '1' {
            totalOnes++
        }
    }
    
    for i := 0; i < len(s)-1; i++ {
        if s[i] == '0' {
            leftZeros++
        } else {
            leftOnes++
        }
        
        result = max(result, leftZeros + totalOnes - leftOnes)
    }
    
    return result
}

func max(a, b int) int {
    if a > b {
        return a
    }
    
    return b
}