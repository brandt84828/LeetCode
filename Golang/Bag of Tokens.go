func bagOfTokensScore(tokens []int, power int) int {
    res, cur := 0, 0
    sort.Ints(tokens)
    for len(tokens) != 0 && (tokens[0] <= power || cur != 0) {
        if tokens[0] <= power {
            power -= tokens[0]
            tokens = tokens[1:]
            cur++
        } else {
            power += tokens[len(tokens)-1]
            tokens = tokens[:len(tokens)-1]
            cur--
        }
        if res < cur {
            res = cur
        }
    }
    return res
}