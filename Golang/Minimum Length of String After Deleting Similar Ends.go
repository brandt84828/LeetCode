func minimumLength(s string) int {
    left, right := 0, len(s)-1
    for left < right && s[left] == s[right] {
        char := s[left]
        for left <= right && s[left] == char {
            left++
        }
        for right >= left && s[right] == char {
            right--
        }
    }
    return right - left + 1
}