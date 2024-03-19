func maxFrequencyElements(nums []int) int {
    var f [101]int
    max := 0
    res := 0
    
    for _, n := range nums {
        f[n]++
        if f[n] == max {
            res += max
        } else if f[n] > max { 
            max = f[n]
            res = max
        }
    } 
    return res
}