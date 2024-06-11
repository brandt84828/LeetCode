//1
func convertToTitle(columnNumber int) string {
    s := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res := ""
    for columnNumber > 0 {
        columnNumber--
        res = string(s[columnNumber % 26]) + res
        columnNumber /= 26
    }
    return res
}

//2
func convertToTitle(columnNumber int) string {
    res := ""

    for columnNumber > 0 {
        columnNumber -= 1
        remainder := columnNumber % 26
        res = string('A'+remainder) + res
        columnNumber /= 26
    }

    return res
}