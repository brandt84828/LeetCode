func longestPalindrome(s string) string {
    res := ""
    for i:=0;i<len(s);i++{
        tmp := helper(s, i, i)
        //odd aba
        if len(tmp) > len(res) {
            res = tmp
        }

        //even abba
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res) {
            res = tmp
        }
    }
    return res
}

func helper(s string ,l int ,r int) string {
    for l >= 0 && r < len(s) && s[l] == s[r] {
        l--
        r++
    }
    return s[l+1:r]
}