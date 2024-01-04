func numJewelsInStones(jewels string, stones string) int {
    count := 0
    result := make(map[rune]int)

    for _, v := range stones{
        if _, ok := result[v]; ok {
            result[v] = result[v] + 1
        } else {
            result[v] = 1
        }
    }

    for _, v := range jewels{
        if times, ok := result[v]; ok {
            count = count + times
        }
    }

    return count
}