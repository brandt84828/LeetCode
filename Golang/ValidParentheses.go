func isValid(s string) bool {
    m := make(map[rune]rune)

    m['('] = ')'
    m['['] = ']'
    m['{'] = '}'
    
    stack := make([]rune,0)
    for _, v := range s {
        if _, ok := m[v]; ok {
            stack = append(stack, v)
        } else if len(stack) > 0 && m[stack[len(stack)-1]] == v {
            stack = stack[:len(stack)-1]
        } else {
            return false
        }
    }

    return len(stack) == 0

}