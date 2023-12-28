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


# Clear
func maxProfit(prices []int) int {
    profit := 0
    minPrice := prices[0]
    
    for i := 1; i < len(prices); i++ {
        if prices[i] < minPrice {
            minPrice = prices[i]
        } else if (prices[i] - minPrice) > profit {
            profit = prices[i] - minPrice
        }
    }
    
    return profit
}