func subsetXORSum(nums []int) int {
    bits := 0
    for _, n := range nums {
        bits |= n
    }
    return bits * int(math.Pow(2.0, float64(len(nums)-1)))
}