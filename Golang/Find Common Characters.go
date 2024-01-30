func commonChars(words []string) []string {
    var res []string
    
    arr := make([][26]byte, len(words))
    
    for i := 0; i < len(words); i++ {
        for j := 0; j < len(words[i]); j++ {
            arr[i][words[i][j] - 'a']++
        }
    }
    
    for i := 0; i < 26; i++ {
        isValid, count := true, 1<<63-1
        
        for j := 0; j < len(words); j++ {
            if arr[j][i] <= 0 {
                isValid = false
                break
            } else if int(arr[j][i]) < count {
                count = int(arr[j][i])
            }
        }
        
        if isValid {
            for count > 0 {
                res = append(res, fmt.Sprintf("%c", i + 'a'))
                count--
            }
        }
    }
    
    return res
}