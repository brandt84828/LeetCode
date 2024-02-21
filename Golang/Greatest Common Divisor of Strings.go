//1
func gcdOfStrings(s1 string, s2 string) string {
    if s1 + s2 != s2 + s1 {
        return ""
    }
    x := gcd(len(s1), len(s2))
    return s1[:x]
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a % b
    }
    return a
}

//2
func gcdOfStrings(str1 string, str2 string) string {
    if str1 == str2 {
        return str1
    }

    if len(str2) > len(str1) {
        str1, str2 = str2, str1
    }

    if str1[:len(str2)] != str2 {
        return ""
    }

    return gcdOfStrings(str1[len(str2):], str2)
}