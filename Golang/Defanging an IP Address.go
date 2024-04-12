func defangIPaddr(address string) string {
    res := ""

    for _, s := range address {
        if s == '.' {
            res += "[.]"
        } else {
            res += string(s)
        }
    }
    return res
}