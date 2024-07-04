func longestPalindrome(s string) int {
    count := make(map[byte]int)
    for i:=0; i<len(s);i++{
          count[s[i]] += 1
    }
    
    ans := 0
    for _, val := range count {
        ans += val / 2 * 2
        if ans % 2 == 0 && val % 2 == 1 {
            ans += 1
        }
    }
    
    return ans
}