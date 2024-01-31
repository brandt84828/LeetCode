//1
func buyChoco(prices []int, money int) int {
    sort.Ints(prices)
    min := prices[0] + prices[1]

    if money >= min {
        return money - min
    }
    
    return money
}

//2
func buyChoco(prices []int, money int) int {
    firstMin := 100
    secondMin := 100

    for _, price := range prices {
        if price < firstMin {
            secondMin = firstMin
            firstMin = price
        } else if price < secondMin {
            secondMin = price
        }
    }

    min := firstMin + secondMin

    if money - min >= 0 {
        return money - min
    } 

    return money
}