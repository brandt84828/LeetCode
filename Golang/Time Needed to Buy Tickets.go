func timeRequiredToBuy(tickets []int, k int) int {
    total := 0
    for index, _ := range tickets {
        if index <= k {
            total += min(tickets[index], tickets[k])
        } else {
            total += min(tickets[index], tickets[k]-1)
        }
    }
    return total
}

func min(a , b int) int {
    if a < b {
        return a
    }
    return b
}s