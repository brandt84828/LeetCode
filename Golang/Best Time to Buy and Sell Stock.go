func maxProfit(prices []int) int {
    res := 0
    lowest := prices[0]
    for _, price := range prices {
        if price < lowest {
            lowest = price
        }
        res = max(res, price - lowest)
    }
    return res
}

func max(a int, b int) int {
    if a < b {
        return b
    }
    return a
}