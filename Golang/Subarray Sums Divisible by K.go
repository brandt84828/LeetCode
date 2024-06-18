func subarraysDivByK(nums []int, k int) int {
    var ans int = 0
    var sum int = 0
    Map := make(map[int]int)
    Map[0] = 1
    for i := 0; i < len(nums); i++ {
        sum = (((sum + nums[i]) % k) + k) % k
        ans += Map[sum]
        Map[sum]++
    }
    return ans
}