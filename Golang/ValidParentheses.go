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

#2

func isValid(s string) bool {
    mapping := make(map[rune]rune)
    mapping[')'] = '('
    mapping[']'] = '['
    mapping['}'] = '{'
    stack := make([]rune,0)

    for _, c := range s {
        if _, ok := mapping[c]; ok && len(stack) > 0 {
            if mapping[c] == stack[len(stack)-1] {
                stack = stack[:len(stack)-1]
                continue
            } else {
                stack = stack[:len(stack)-1]
                return false
            }
        } else {
            stack = append(stack, c)
        }
    }
    return len(stack) == 0
}