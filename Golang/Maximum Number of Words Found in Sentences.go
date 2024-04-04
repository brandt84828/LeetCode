func mostWordsFound(sentences []string) int {
    ma := 0
    for _, s := range sentences {
        slice := strings.Split(s, " ")
        ma = max(ma, len(slice))
    }
    return ma
}

func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}