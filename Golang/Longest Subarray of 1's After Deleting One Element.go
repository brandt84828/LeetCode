func longestSubarray(nums []int) int {
	l, r := 0, 0
    zeroes := 0
    for ; r < len(nums); r++ {
        if nums[r] == 0 {
            zeroes++
        }
        if zeroes > 1 {
            if nums[l] == 0 {
                zeroes--
            }
            l++
        }
    }
    return r - l - 1
}