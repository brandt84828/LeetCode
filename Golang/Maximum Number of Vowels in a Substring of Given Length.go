func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func maxVowels(s string, k int) int {
    vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}
    count := 0

    for i := 0; i < k; i++ {
        if vowels[rune(s[i])] {
            count++
        }
    }

    ans := count

    for i := k; i < len(s); i++ {
        if vowels[rune(s[i])] {
            count++
        }
        if vowels[rune(s[i-k])] {
            count--
        }

        ans = max(ans, count)
    }

    return ans
}