func decodeString(s string) string {
    stack := []string{}
    var numStr, subStr string
    for _, ch := range s {
        if ch != ']' {
            stack = append(stack, string(ch))
            continue
        }
        for len(stack) > 0 && stack[len(stack)-1] != "[" {
            subStr = stack[len(stack)-1] + subStr
            stack = stack[:len(stack)-1]
        }
        stack = stack[:len(stack)-1]
        for len(stack) > 0 && stack[len(stack)-1] >= "0" && stack[len(stack)-1] <= "9" {
            numStr = stack[len(stack)-1] + numStr
            stack = stack[:len(stack)-1]
        }
        num, _ := strconv.Atoi(numStr)
        for i := 0; i < num; i++ {
            stack = append(stack, subStr)
        }
        numStr, subStr = "", ""
    }
    return strings.Join(stack, "")
}