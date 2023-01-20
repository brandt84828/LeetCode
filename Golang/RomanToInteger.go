func romanToInt(s string) int {

    roman := map[byte]int{'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    total := 0

    for i:=0; i < len(s) - 1; i++ {
        if s[i] == 'I' && (s[i+1] == 'V' || s[i+1] == 'X') {
            total = total - 1
        } else if s[i] == 'X' && (s[i+1] == 'L' || s[i+1] == 'C') {
            total = total - 10
        } else if s[i] == 'C' && (s[i+1] == 'D' || s[i+1] == 'M') {
            total = total - 100
        } else {
            total = total + roman[s[i]]
        }
    }

    total = total + roman[s[len(s) - 1]]

    return total
    
}