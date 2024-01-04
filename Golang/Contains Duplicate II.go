func containsNearbyDuplicate(nums []int, k int) bool {
    ans := make(map[int]int)

    for i, v := range nums {
        if value, ok := ans[v]; ok {
            if absInt(i, value) <= k {
                return true
            } else {
                ans[v] = i
            }
        } else {
            ans[v] = i
        }
    }

    return false
}

func absInt(a, b int) int {
    if a - b < 0 {
        return b - a
    }
    
    return a - b
}