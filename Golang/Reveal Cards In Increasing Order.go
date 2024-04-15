func deckRevealedIncreasing(deck []int) []int {
    sort.Ints(deck)
    n, indx := len(deck), 0
    result, queue := make([]int, n), make([]int, n)
    for i := 0; i < n; i++ {
        queue[i] = i
    }

    for len(queue) > 0 {
        result[queue[0]] = deck[indx]
        indx++
        queue = queue[1:]
        if len(queue) > 0 {
            queue = append(queue[1:], queue[0])
        }
    }
    return result
}