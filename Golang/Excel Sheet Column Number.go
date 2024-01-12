func titleToNumber(columnTitle string) int {
    total := 0

    for _, column := range columnTitle {
        d := int(column - 'A' + 1)
        total = total * 26 + d
    }

    return total
}