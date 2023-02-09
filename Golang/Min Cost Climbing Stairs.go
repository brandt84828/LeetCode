func minCostClimbingStairs(cost []int) int {
    for i:=len(cost)-3;i > -1;i-- {
        cost[i] = cost[i] + min(cost[i+1], cost[i+2])
    }
    return min(cost[0], cost[1])
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}