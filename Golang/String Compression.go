func compress(chars []byte) int {
    walker, runner := 0, 0
    for runner < len(chars){
        chars[walker] = chars[runner]
        count := 1

        for runner + 1 < len(chars) && chars[runner] == chars[runner + 1] {
            runner++
            count++
        }

        if count > 1 {
            for _, v := range strconv.Itoa(count) {
                chars[walker + 1] = byte(v)
                walker++
            }
        }

        runner++
        walker++
    }
    return walker
}