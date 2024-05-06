func numSubarrayProductLessThanK(nums []int, k int) int {
    left := 0
    prod := 1
    count :=  0

    for right:=0;right<len(nums);right++ {
        prod *=  nums[right]
        for prod >= k && left <= right {
            prod /= nums[left]
            left++
        }
        count += right - left + 1
    }
    return count
}