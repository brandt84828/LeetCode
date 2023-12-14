func maximumWealth(accounts [][]int) int {
    maxWealth := 0
    for i:=0; i < len(accounts);i++ {
        temp := 0
        for j:=0; j < len(accounts[i]);j++{
            temp = temp + accounts[i][j]
        }
        if temp > maxWealth {
            maxWealth = temp
        }
    }
    return maxWealth
}
