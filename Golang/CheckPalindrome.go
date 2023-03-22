func check_if_palindrome(s string) bool {
    left := 0
    right := len(s) - 1
    for left < right {
        if s[left] != s[right] {
            return false
        }
        left = left + 1
        right = right - 1
    }
    return true
}