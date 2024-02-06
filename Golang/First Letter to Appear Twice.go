//1
func repeatedCharacter(s string) byte {
    set:=make(map[byte]string)
    for i:=0;i<len(s);i++{
      if _,ok:=set[s[i]];ok{
        return s[i]
      }
		set[s[i]] = ""
    }
    return ' '
}

//2
func repeatedCharacter(s string) byte {
    m := map[rune]bool{}

    for _, char := range s {
        if _, ok := m[char]; ok {
            return byte(char)
        }
        m[char] = true
    }
    return byte('s')
}