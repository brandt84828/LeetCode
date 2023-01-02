func isAnagram(s string, t string) bool {

    hash := make(map[rune]int)

    for _, v := range s {
        hash[v]++
    }
        
    for _, v := range t {
        hash[v]--
    }


    for _, v := range hash {
        if v != 0 {
            return false
        }
    }
    return true 
}