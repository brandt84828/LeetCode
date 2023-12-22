func lengthOfLastWord(s string) int {
    
    n := len(s)
    count := 0

    for i:=n-1;i>=0;i--{
        if count == 0 && s[i] == ' ' {
            continue
        } else {
            if s[i] == ' '{
                break
            }
        }
        count++
    }
    return count
}