func zeroFilledSubarray(nums []int) int64 {
    var total, zero_count int64 = 0, 0
    for _, num := range(nums) {
        if num == 0 {
            zero_count = zero_count + 1
            total = total + zero_count
        } else {
            zero_count = 0
        }
    }
    return total
}